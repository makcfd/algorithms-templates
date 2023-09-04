from collections.abc import Callable

"""
ID of package:
89739934
"""

test="""6
6
push_front 10
push_front 20
push_back 99
push_back 88
pop_back
pop_back""".split('\n')

test_2="""7
10
push_front -855
push_front 0
pop_back
pop_back
push_back 844
pop_back
push_back 823""".split('\n')

def input():
    global test
    return test.pop(0)
"""
В первой строке записано количество команд n — int <= 100000. 
Во второй строке записано число m — max size <= 50000. 
В следующих n строках записана одна из команд:
push_back(value) – добавить элемент в конец дека.
Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека.
Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error»."""

DEBUG = False


def debug_mode(func: Callable):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        if DEBUG:
            print(deck.deck)
        return result
    return wrapped


class Deque:

    def __init__(self, n):
        self.deck = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    @debug_mode
    def push_front(self, x):
        "filling in from right to left towards the head"
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.deck[self.head] = x
            self.size += 1
        else:
            print("error")

    @debug_mode
    def push_back(self, x):
        "filling in from left to right towards the tail"
        if self.size != self.max_n:
            self.deck[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print("error")

    @debug_mode
    def pop_front(self):
        "classic pop for a queue"
        if self.is_empty():
            return "error"
        x = self.deck[self.head]
        self.deck[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    @debug_mode
    def pop_back(self):
        ""
        if self.is_empty():
            return "error"
        self.tail = (self.tail - 1) % self.max_n
        x = self.deck[self.tail]
        self.deck[self.tail] = None
        self.size -= 1
        return x

    def size(self):
        return self.size

    def __str__(self) -> str:
        return self.deck


if __name__ == '__main__':
    number = int(input())
    deque_size = int(input())
    deque = Deque(deque_size)
    for _ in range(number):
        command = input().split()
        if len(command) == 1:
            result = getattr(deque, command[0])()
            if result is not None:
                print(result)
        elif len(command) == 2:
            getattr(deque, command[0])(command[1])
        # print(f"command is: {command}")
        # if command[0] == "push_front":
        #     deque.push_front(command[1])
        # elif command[0] == "push_back":
        #     deque.push_back(command[1])
        # elif command[0] == "pop_back":
        #     print(deque.pop_back())
        # elif command[0] == "pop_front":
        #     print(deque.pop_front())
        # elif command[0] == "size":
        #     print(deque.size())
        # print()
