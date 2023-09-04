# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing


"""

get() — вывести элемент, находящийся в голове очереди, и удалить его.
Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
"""

test = """10
put -34
put -23
get
size
get
size
get
get
put 80
size""".split('\n')


def input():  # функция переопределена в тестовых целях для замены ручного ввода
    global test
    return test.pop(0)


class QueueLinkedList:
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
    qll = QueueLinkedList()
    number = int(input())
    for _ in range(number):
        command = input().split()
        if command[0] == "put":
            print(qll.put(command[1]))
        elif command[0] == "get":
            print(qll.get())
        elif command[0] == "size":
            print(qll.size())
