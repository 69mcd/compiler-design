class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class QuadrupleCodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.quadruples = []

    def generate_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def generate_quadruple(self, op, arg1, arg2, result):
        self.quadruples.append((op, arg1, arg2, result))

    def generate_code(self, node):
        if node is None:
            return None

        if node.value in ['+', '-', '*', '/']:
            left_temp = self.generate_code(node.left)
            right_temp = self.generate_code(node.right)
            if left_temp and right_temp:
                temp = self.generate_temp()
                self.generate_quadruple(node.value, left_temp, right_temp, temp)
                return temp
        else:
            return node.value

    def print_quadruples(self):
        print("Quadruple Representation:")
        print("{:<10} {:<10} {:<10} {:<10}".format("Operator", "Argument 1", "Argument 2", "Result"))
        for op, arg1, arg2, result in self.quadruples:
            print("{:<10} {:<10} {:<10} {:<10}".format(op, arg1, arg2, result))

class TripleCodeGenerator(QuadrupleCodeGenerator):
    def generate_quadruple(self, op, arg1, arg2, result):
        if op != 'ASSIGN':
            super().generate_quadruple(op, arg1, arg2, result)
        else:
            self.quadruples.append((op, arg1, None, result))

    def print_quadruples(self):
        print("\nTriple Representation:")
        print("{:<10} {:<10} {:<10}".format("Operator", "Argument", "Result"))
        for op, arg1, _, result in self.quadruples:
            print("{:<10} {:<10} {:<10}".format(op, arg1, result))

# Example usage
expression_tree = Node('+')
expression_tree.left = Node('3')
expression_tree.right = Node('*')
expression_tree.right.left = Node('4')
expression_tree.right.right = Node('5')

quadruple_generator = QuadrupleCodeGenerator()
quadruple_generator.generate_code(expression_tree)
quadruple_generator.print_quadruples()

triple_generator = TripleCodeGenerator()
triple_generator.generate_code(expression_tree)
triple_generator.print_quadruples()
