"""
ID of package:
90079417
"""


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self):
        self._items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self._items.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return EmptyStackError("Stack is empty")
        self.size -= 1
        return self._items.pop()


def evaluate_expression(tokens):
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
