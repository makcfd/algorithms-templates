# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
test="""4
4
push_front 861
push_front -819
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
    global test_2
    return test_2.pop(0)
"""
В первой строке записано количество команд n — целое число, 
не превосходящее 100000. 
Во второй строке записано число m — максимальный размер дека. 
Он не превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека.
Если в деке уже находится максимальное число элементов, вывести «error».

push_front(value) – добавить элемент в начало дека.
Если в деке уже находится максимальное число элементов, вывести «error».

pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».

pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».

Value — целое число, по модулю не превосходящее 1000."""

class Deque:
    def __init__(self, max_size):
        self.buffer = [None] * max_size
        self.max_size = max_size
        self.size = 0
        self.front = 0
        self.back = 0

    def push_front(self, value):
        if self.size == self.max_size:
            return "error"
        self.front = (self.front - 1) % self.max_size
        self.buffer[self.front] = value
        self.size += 1

    def push_back(self, value):
        if self.size == self.max_size:
            return "error"
        self.buffer[self.back] = value
        self.back = (self.back + 1) % self.max_size
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return "error"
        value = self.buffer[self.front]
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return value

    def pop_back(self):
        if self.size == 0:
            return "error"
        self.back = (self.back - 1) % self.max_size
        value = self.buffer[self.back]
        self.size -= 1
        return value

n = int(input())
max_size = int(input())
deque = Deque(max_size)

for i in range(n):
    command = input().split()
    if command[0] == "push_front":
        deque.push_front(int(command[1]))
    elif command[0] == "push_back":
        deque.push_back(int(command[1]))
    elif command[0] == "pop_front":
        print(deque.pop_front())
    elif command[0] == "pop_back":
        print(deque.pop_back())

# if __name__ == '__main__':
#     number = int(input())
#     deck_size = int(input())
#     deck = Deck(deck_size)
#     for _ in range(number):
#         command = input().split()
#         if command[0] == "push_front":
#             deck.push_front(command[1])
#         elif command[0] == "push_back":
#             deck.push_back(command[1])
#         elif command[0] == "pop_back":
#             print(deck.pop_back())
#         elif command[0] == "push_front":
#             print(deck.push_front())
#         elif command[0] == "size":
#             print(deck.size())
