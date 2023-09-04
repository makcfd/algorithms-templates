test = """4 7
3 2 6 4
1 3
2 5
3 7
4 10
5 5
6 100
9 2""".split('\n')


def input():
    global test
    return test.pop(0)


import heapq

nun_of_proc, num_of_task = map(int, input().split())
processors = list(map(int, input().split()))

processors = [(power, idx) for idx, power in enumerate(processors)]
processors.sort()

heap = []

total_energy = 0

for _num_task in range(num_of_task):
    time_arrival, len_taks = map(int, input().split())
    while heap and heap[0][0] <= time_arrival:
        _, freed_idx = heapq.heappop(heap)
    if len(heap) == nun_of_proc:
        continue
    _, chosen_idx = processors[len(heap)]
    total_energy += processors[len(heap)][0] * len_taks
    heapq.heappush(heap, (time_arrival + len_taks, chosen_idx))

print(total_energy)
