import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, element):
        heapq.heappush(self.queue, element)

    def pop(self):
        if self.queue:
            # intermediate_result = self.peek()
            # if (intermediate_result[1] + intermediate_result[2]) < arrival_time:
            return heapq.heappop(self.queue)
        else:
            return None

    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def __str__(self):
        return str(self.queue)


pq = PriorityQueue()
# initial state of processors
pq.insert((0, 2))
pq.insert((0, 3))
pq.insert((0, 4))
pq.insert((0, 6))
print(pq)
pq.pop()
pq.insert((4, 2))
print(pq)
pq.pop()
pq.insert((7, 3))
print(pq)
pq.pop()
pq.insert((10, 4))
print(pq.peek())
