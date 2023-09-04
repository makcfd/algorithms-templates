test = """5
push -9
get_max
pop
get_max
get_max""".split('\n')
# test = """2
# push 1
# pop
# """.split('\n')


def input():  # функция переопределена в тестовых целях для замены ручного ввода
    global test
    return test.pop(0)

class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        #return self.items.remove(self.items[-1]) if self.items else "error"
        if not self.items:
            return "error"
        self.items.pop()
        pass

    def get_max(self):
        return max(self.items) if self.items else None

    def __repr__(self) -> str:
        return self.items


if __name__ == "__main__":
    stack = StackMax()
    number = int(input())
    results = []
    for _ in range(number):
        command = input().split()
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            pop_result = stack.pop()
            results.append(pop_result) if pop_result else _
            #results.append(pop_result)
        if command[0] == "get_max":
            results.append(stack.get_max())

    for result in results:
        print(result)
