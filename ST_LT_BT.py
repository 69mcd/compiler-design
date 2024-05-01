class Assembler:
    def __init__(self):
        self.symbol_table = {}
        self.literal_table = {}
        self.base_table = {}
        self.current_address = 0

    def process_instruction(self, instruction):
        opcode = instruction[0]
        if opcode not in ['START', 'END', 'ORG']:
            if len(instruction) > 1:
                if instruction[1].isdigit():
                    self.literal_table[self.current_address] = instruction[1]
                else:
                    self.symbol_table[instruction[1]] = self.current_address

    def assemble(self, lines):
        machine_code = []

        for line in lines:
            parts = line.split()
            if len(parts) > 0:
                if parts[0] == 'START':
                    self.current_address = int(parts[1])
                elif parts[0] == 'ORG':
                    self.current_address = int(parts[1])
                elif parts[0] == 'END':
                    break
                else:
                    instruction = parts[1:]
                    self.process_instruction(instruction)
                    machine_code.append((self.current_address, ' '.join(instruction)))
                    self.current_address += 1

        return machine_code

    def print_tables(self):
        print("Symbol Table:")
        for symbol, address in self.symbol_table.items():
            print(f"{symbol}: {address}")

        print("\nLiteral Table:")
        for address, value in self.literal_table.items():
            print(f"{value}: {address}")


# Example usage
asm = Assembler()
program = [
    "START 100",
    "ORG 100",
    "LOOP MOV R1, A",
    "A DC 10",
    "END"
]
machine_code = asm.assemble(program)
for address, instruction in machine_code:
    print(f"{address}: {instruction}")

asm.print_tables()
