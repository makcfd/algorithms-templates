# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
test="""2 1 + 3 *""".split('\n')

"""
ID of package:
89742090
"""

def input():
    global test
    return test.pop(0)

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
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return self.items


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


if __name__ == '__main__':

    combinations = input().split()
    print(evaluate_expression(combinations))
