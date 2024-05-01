def constant_propagation_and_dead_code_elimination(code):
    # Step 1: Constant Propagation
    constants = {}
    updated_code = ""
    for line in code.split("\n"):
        if "=" in line:
            var, exp = line.split("=")
            var = var.strip()
            exp = exp.strip()
            if all([c.isdigit() for c in exp]):
                constants[var] = eval(exp)
            else:
                for const_var, const_val in constants.items():
                    exp = exp.replace(const_var, str(const_val))
                updated_code += var + " = " + exp + "\n"
        else:
            updated_code += line + "\n"

    # Step 2: Dead Code Elimination
    new_code_lines = []
    for line in updated_code.split("\n"):
        if "w =" not in line:
            new_code_lines.append(line)
    updated_code = "\n".join(new_code_lines)

    return updated_code


# Example:
code = """
x = 5
y = x + 3
z = y * 2
w = 11
result = z + w
"""
updated_code = constant_propagation_and_dead_code_elimination(code)
print(updated_code)
