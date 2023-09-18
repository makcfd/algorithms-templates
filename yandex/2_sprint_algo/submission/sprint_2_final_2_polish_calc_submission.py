"""
ID of package:
90773738
"""


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


class EmptyStackError(Exception):
    """Exception raised when a Stack has no elements left."""
    pass


class Stack:
    """Stack interface over a list to add and remove elements."""
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return EmptyStackError("Stack is empty")
        return self._items.pop()


def evaluate_expression(tokens):
    """Calculator based on Reversed Polish Notaion."""
    stack = Stack()
    for token in tokens:
        if token in operations:
            b = stack.pop()
            a = stack.pop()
            operation = operations[token]
            result = operation(a, b)
            stack.push(result)
        else:
            stack.push(int(token))
    return stack.pop()


if __name__ == "__main__":
    combinations = input().split()
    print(evaluate_expression(combinations))
