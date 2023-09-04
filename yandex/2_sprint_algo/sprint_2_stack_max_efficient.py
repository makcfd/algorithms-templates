test = """10
pop
pop
push 4
push -5
push 7
pop
pop
get_max
pop
get_max""".split('\n')


def input():
    global test
    return test.pop(0)


class StackMaxEfficient:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        self.items.append(item)
        if not self.max_items or item > self.max_items[-1]:
            self.max_items.append(item)
        else:
            self.max_items.append(self.max_items[-1])

    def pop(self):
        if not self.items:
            return "error"
        self.items.pop()
        self.max_items.pop()

    def get_max(self):
        return self.max_items[-1] if self.max_items else None


if __name__ == "__main__":
    stack = StackMaxEfficient()
    number = int(input())
    for _ in range(number):
        command = input().split()
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            pop_result = stack.pop()
            if pop_result:
                print(pop_result)
        elif command[0] == "get_max":
            print(stack.get_max())
