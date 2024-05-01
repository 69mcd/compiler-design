# Pass 1: Generate symbol table
def pass1(input_lines):
    symbol_table = {}
    location_counter = 0

    for line in input_lines:
        parts = line.split()
        if len(parts) > 0:
            if parts[0] not in ['START', 'END']:
                if parts[0] not in symbol_table:
                    symbol_table[parts[0]] = location_counter
                location_counter += 1

    return symbol_table


# Pass 2: Generate machine code using symbol table
def pass2(input_lines, symbol_table):
    machine_code = []

    for line in input_lines:
        parts = line.split()
        if len(parts) > 0:
            if parts[0] == 'START':
                location_counter = int(parts[1])
            elif parts[0] == 'END':
                break
            else:
                instruction = ""
                if len(parts) > 1:
                    if parts[1] in symbol_table:
                        instruction += str(symbol_table[parts[1]])
                    else:
                        instruction += parts[1]
                if len(parts) > 2:
                    instruction += " "
                    if parts[2] in symbol_table:
                        instruction += str(symbol_table[parts[2]])
                    else:
                        instruction += parts[2]
                machine_code.append(instruction)

    return machine_code


# Example input
input_lines = [
    "LOOP1 START 100",
    "MOV A, 0",
    "ADD A, B",
    "END",
    "LOOP2 START 200",
    "MOV B, 5",
    "SUB A, B",
    "END"
]

# Pass 1: Generate symbol table
symbol_table = pass1(input_lines)
print("Symbol Table:")
print(symbol_table)

# Pass 2: Generate machine code using symbol table
machine_code = pass2(input_lines, symbol_table)
print("\nMachine Code:")
for instruction in machine_code:
    print(instruction)
