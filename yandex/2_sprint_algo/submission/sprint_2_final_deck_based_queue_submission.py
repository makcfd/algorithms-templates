"""
ID of package:
90077606
"""


class EmptyDequeError(Exception):
    pass


class FullDequeError(Exception):
    pass


class Deque:

    def __init__(self, n):
        self._deque = [None] * n
        self._max_n = n
        self._head = 0
        self._tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, x):
        """Filling in from right to left towards the head."""
        if self.size != self._max_n:
            self._head = (self._head - 1) % self._max_n
            self._deque[self._head] = x
            self.size += 1
        else:
            raise FullDequeError("error")

    def push_back(self, x):
        """Filling in from left to right towards the tail."""
        if self.size != self._max_n:
            self._deque[self._tail] = x
            self._tail = (self._tail + 1) % self._max_n
            self.size += 1
        else:
            print("error")

    def pop_front(self):
        """Classic pop for a queue."""
        if self.is_empty():
            raise EmptyDequeError("error")
        x = self._deque[self._head]
        self._deque[self._head] = None
        self._head = (self._head + 1) % self._max_n
        self.size -= 1
        return x

    def pop_back(self):
        """Reverted pop from a queue."""
        if self.is_empty():
            raise EmptyDequeError("error")
        self._tail = (self._tail - 1) % self._max_n
        x = self._deque[self._tail]
        self._deque[self._tail] = None
        self.size -= 1
        return x

    def size(self):
        return self.size

    def __str__(self) -> str:
        return self._deque


if __name__ == "__main__":
    number = int(input())
    deck_size = int(input())
    deck = Deque(deck_size)
    for _ in range(number):
        command = input().split()
        try:
            if len(command) == 1:
                result = getattr(deck, command[0])()
                if result is not None:
                    print(result)
            elif len(command) == 2:
                getattr(deck, command[0])(command[1])
        except (EmptyDequeError, FullDequeError) as error:
            print(error)
