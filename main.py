#Узлы
class Node:
    pass

class Num(Node):
    def __init__(self, value):
        self.value = value

class Add(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Mul(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

#Посетитель
class PrintVisitor:
    def visit(self, node):
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name)
        return visitor(node)

    def visit_Num(self, node):
        return str(node.value)

    def visit_Add(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return '({} + {})'.format(left, right)

    def visit_Mul(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return '({} * {})'.format(left, right)

#Посетитель счётчик
class CalcVisitor:
    def visit(self, node):
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name)
        return visitor(node)

    def visit_Num(self, node):
        return node.value

    def visit_Add(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return left + right

    def visit_Mul(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return left * right

#Посетитель сте(й)ка
class StackVisitor:
    def visit(self, node):
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name)
        return visitor(node)

    def visit_Num(self, node):
        return "PUSH " + str(node.value)

    def visit_Add(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return '{}\n{}\nADD'.format(left, right)

    def visit_Mul(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return '{}\n{}\nMUL'.format(left, right)


if __name__ == '__main__':
    ast = Add(Num(7), Mul(Num(3), Num(2)))
    pv = PrintVisitor()
    print(pv.visit(ast))
    cv = CalcVisitor()
    print(cv.visit(ast))
    sv = StackVisitor()
    print(sv.visit(ast))

