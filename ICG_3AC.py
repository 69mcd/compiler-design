class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ThreeAddressCodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def generate_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def generate_code(self, node):
        if node is None:
            return None

        if node.value in ['+', '-', '*', '/']:
            left_temp = self.generate_code(node.left)
            right_temp = self.generate_code(node.right)
            if left_temp and right_temp:
                temp = self.generate_temp()
                self.code.append((node.value, left_temp, right_temp, temp))
                return temp
        else:
            return node.value

# Example usage
expression_tree = Node('+')
expression_tree.left = Node('3')
expression_tree.right = Node('*')
expression_tree.right.left = Node('4')
expression_tree.right.right = Node('5')

generator = ThreeAddressCodeGenerator()
generator.generate_code(expression_tree)
for op, arg1, arg2, result in generator.code:
    print(f" operator {op} args1 {arg1} args2 {arg2} result {result}")
