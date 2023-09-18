"""
ID of package:
90777870
"""


class EmptyDequeError(Exception):
    """Exception raised when a Deque has no elements left."""
    pass


class FullDequeError(Exception):
    """Exception raised when a Deque is full."""
    pass


class Deque:
    """Deque interface over a list to add and remove
    elements from two sides: back and front.
    """

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
        if self.size == self._max_n:
            raise FullDequeError("error")
        self._head = (self._head - 1) % self._max_n
        self._deque[self._head] = x
        self.size += 1

    def push_back(self, x):
        """Filling in from left to right towards the tail."""
        if self.size == self._max_n:
            raise FullDequeError("error")
        self._deque[self._tail] = x
        self._tail = (self._tail + 1) % self._max_n
        self.size += 1

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
    deque_size = int(input())
    deque = Deque(deque_size)
    for _ in range(number):
        command, *args = input().split()
        try:
            (getattr(deque, command)(*args) if args else
             print(getattr(deque, command)()))
        except (EmptyDequeError, FullDequeError) as error:
            print(error)
