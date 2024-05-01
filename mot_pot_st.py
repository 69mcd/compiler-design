class Assembler:
    def __init__(self):
        self.mot = {
            'MOV': '0001',
            'ADD': '0010',
            'SUB': '0011',
            # Add more instructions as needed
        }
        self.pot = {
            'START': '0001',
            'END': '0002',
            'ORG': '0003',
            'DB': '0004',
            # Add more pseudo-ops as needed
        }
        self.symbol_table = {}

    def process_instruction(self, instruction):
        if instruction[0] in self.mot:
            opcode = self.mot[instruction[0]]
            if len(instruction) > 1:
                operand = instruction[1]
                # Check if operand is a label
                if operand in self.symbol_table:
                    operand_address = self.symbol_table[operand]
                else:
                    operand_address = operand
                return opcode + ' ' + operand_address
            else:
                return opcode
        elif instruction[0] in self.pot:
            pseudo_opcode = self.pot[instruction[0]]
            if len(instruction) > 1:
                operand = instruction[1]
                if instruction[0] == 'DB':
                    return pseudo_opcode + ' ' + operand
                # Handle other pseudo-ops if needed
            else:
                return pseudo_opcode

    def assemble(self, lines):
        machine_code = []
        current_address = 0

        for line in lines:
            parts = line.split()
            if len(parts) > 0:
                if parts[0] in self.pot:
                    if parts[0] == 'START':
                        current_address = int(parts[1])
                    elif parts[0] == 'END':
                        break
                    elif parts[0] == 'ORG':
                        current_address = int(parts[1])
                elif len(parts) > 1:
                    label = parts[0]
                    instruction = parts[1:]
                    machine_instruction = self.process_instruction(instruction)
                    if machine_instruction:
                        machine_code.append((current_address, machine_instruction))
                        self.symbol_table[label] = current_address
                        current_address += 1

        return machine_code


# Example usage
asm = Assembler()
program = [
    "START 100",
    "ORG 100",
    "LABEL1 MOV R1, 50",
    "LABEL2 ADD R1, 30",
    "END"
]
machine_code = asm.assemble(program)
for address, instruction in machine_code:
    print(f"{address}: {instruction}")
