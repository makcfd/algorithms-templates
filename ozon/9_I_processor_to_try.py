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
pq.insert((2, 0, 0))
pq.insert((3, 0, 0))
pq.insert((4, 0, 0))
pq.insert((6, 0, 0))
tasks = [(1, 3), (2, 5), (3, 7), (4, 10), (5, 5), (6, 100), (9, 2)]
# pq.insert((2, 1, 3))
# pq.insert((3, 2, 5))
# pq.insert((4, 3, 7))
# pq.insert((2, 4, 10))

print()
print("initial PQ: ", pq)
results = []
top_proc = pq.peek()
print("top_proc:", top_proc)
proc_status = top_proc[1] + top_proc[2]
print("task time arrival:", tasks[0][0])
print("proc_status:", proc_status)
print("Can the top proc be taken:", tasks[0][0] >= proc_status)
taken_proc = pq.pop()
results.append(taken_proc)
print("proc taken out:", taken_proc)
element = (taken_proc[0], tasks[0][0], tasks[0][1])
pq.insert(element)
print("pq after update:", pq)
print("top element:", pq.peek())
# for task in tasks:
#     chekc_proc = pq.peek
#     if task[0] >= (chekc_proc[1] + chekc_proc[2]):
#         proc_taken = pq.pop
#         schedule = (proc_taken[0], task[0], task[1])
#         pq.insert(schedule)

# element = pq.remove()
# print("Removed element:", element)
# print("Removed element:", element[0])
# element = list(element)
# element[1] = 1
# element[2] = 3
# element = tuple(element)
# pq.insert(element)
# print("updated PQ: ", pq)
# print(pq.peek())
# pq.insert((2, 0, 0))
# print(pq.peek())

