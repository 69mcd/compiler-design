class MacroProcessor:
    def __init__(self):
        self.macros = {}

    def define_macro(self, name, args, definition):
        self.macros[name] = (args, definition)

    def expand_macro(self, name, args):
        if name not in self.macros:
            return None

        macro_args, definition = self.macros[name]
        if len(args) != len(macro_args):
            print(f"Error: Incorrect number of arguments for macro {name}")
            return None

        expansion = definition
        for arg_name, arg_value in zip(macro_args, args):
            expansion = expansion.replace(arg_name, arg_value)

        return expansion

    def process(self, input_lines):
        macro_definition = False
        name = ""
        args = []
        definition = []
        output_lines = []
        for line in input_lines:
            parts = line.split()
            if len(parts) > 0 and parts[0] == '%MACRO':
                macro_definition = True
                name = parts[1]
                args = parts[2:]
            elif macro_definition:
                if parts[0] == "%END":
                    macro_definition = False
                    self.define_macro(name, args, "\n".join(definition))
                    name = ""
                    args = []
                    definition = []
                else:
                    definition.append(line)
            else:
                output_lines.append(line)

        expanded_lines = []
        for line in output_lines:
            parts = line.split()
            if len(parts) > 0 and parts[0] in self.macros:
                name = parts[0]
                args = parts[1:]
                expansion = self.expand_macro(name, args)
                if expansion:
                    expanded_lines.extend(expansion.split("\n"))
            else:
                expanded_lines.append(line)

        return expanded_lines


# Example usage
input_lines = [
    "%MACRO ADD a b",
    "    MOV AL, a",
    "    ADD AL, b",
    "%END",
    "ADD 10, 20",
    "MOV BL, 30"
]

processor = MacroProcessor()
output_lines = processor.process(input_lines)
for line in output_lines:
    print(line)
