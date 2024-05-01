class MacroProcessor:
    def __init__(self):
        self.mdt = {}
        self.mnt = {}
        self.ala = {}

    def define_macro(self, name, definition):
        self.mdt[name] = definition

    def expand_macro(self, name, arguments):
        if name in self.mdt:
            definition = self.mdt[name]
            if len(arguments) > 0:
                for i, arg in enumerate(arguments):
                    definition = definition.replace(f'#{i}', arg)
            return definition
        else:
            return f"Error: Macro '{name}' not defined"

    def add_macro_name(self, name, arg_count):
        self.mnt[name] = arg_count

    def add_argument_list(self, name, arguments):
        self.ala[name] = arguments

    def expand_code(self, input_code):
        expanded_code = []
        for line in input_code:
            parts = line.split()
            if len(parts) > 0 and parts[0] in self.mdt:
                macro_name = parts[0]
                arguments = parts[1:]
                expanded_macro = self.expand_macro(macro_name, arguments)
                if expanded_macro:
                    expanded_code.extend(expanded_macro.split('\n'))
            else:
                expanded_code.append(line)
        return expanded_code

    def print_tables(self):
        print("Macro Definition Table (MDT):")
        for name, definition in self.mdt.items():
            print(f"{name}: {definition}")

        print("\nMacro Name Table (MNT):")
        for name, arg_count in self.mnt.items():
            print(f"{name}: {arg_count} arguments")

        print("\nArgument List Array (ALA):")
        for name, arguments in self.ala.items():
            print(f"{name}: {arguments}")

# Example usage
mp = MacroProcessor()
mp.define_macro("LOOP", "MOV R1, #0\nLOOP1: CMP R1, #10\n        JZ ENDLOOP\n        INC R1\n        JMP LOOP1\nENDLOOP: ")
mp.add_macro_name("LOOP", 0)
mp.add_argument_list("LOOP", [])
mp.print_tables()

input_code = [
    "LOOP",
    "MOV A, B",
    "END"
]
expanded_code = mp.expand_code(input_code)
print("\nExpanded code:")
for line in expanded_code:
    print(line)
