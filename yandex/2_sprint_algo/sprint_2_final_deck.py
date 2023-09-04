# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
test="""4
4
push_front 861
push_front -819
pop_back
pop_back""".split('\n')


def input():
    global test
    return test.pop(0)
"""
В первой строке записано количество команд n — целое число, 
не превосходящее 100000. 
Во второй строке записано число m — максимальный размер дека. 
Он не превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000."""

class Deck:
    class Node:
        def __init__(self, value=None, next_item=None):
            self.value = value
            self.next_item = next_item

        def __str__(self) -> str:
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size_ = 0

    def __repr__(self) -> str:
        return self.head

    def is_empty(self):
        return self.size_ == 0

    def get(self):
        if self.is_empty():
            return "error"
        node = self.head.value
        self.size_ -= 1
        self.head = self.head.next_item
        return node

    def put(self, value):
        if self.is_empty():
            self.head = self.Node(value)
            self.tail = self.head
        else:
            self.tail.next_item = self.Node(value)
            self.tail = self.tail.next_item
        self.size_ += 1

    def size(self):
        return self.size_

    def __str__(self) -> str:
        return self.head


if __name__ == '__main__':
    number = int(input())
    deck_size = int(input())
    deck = Deck(deck_size)
    for _ in range(number):
        command = input().split()
        if command[0] == "put":
            print(deck.put(command[1]))
        elif command[0] == "get":
            print(deck.get())
        elif command[0] == "size":
            print(deck.size())