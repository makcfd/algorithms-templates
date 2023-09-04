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


num_processors, num_tasks = map(int, input().split())
energy_consumptions = sorted((int(energy)) for energy in input().split())
tasks = [tuple(map(int, input().split())) for _ in range(num_tasks)]

# Priority queue of processors: (availability time, energy consumption, processor index)

#available_processors = [(0, energy) for priority, energy in enumerate(energy_consumptions)]
available_processors = {key: 0 for key in energy_consumptions}


total_energy_consumed = 0
for task_arrival_time, task_duration in tasks:
    top_proc_aval_time = available_processors[0][1]
    while available_processors and top_proc_aval_time <= task_arrival_time:
        proc_avail_time, priority, proc_energy = heapq.heappop(available_processors)
        if proc_avail_time <= task_arrival_time:
            total_energy_consumed += proc_energy * task_duration
            print("task_arrival_time, task duration:", task_arrival_time, task_duration)
            print("proc_energy: ", proc_energy)
            print("energy consumption increment: ", proc_energy * task_duration)
            print("total_energy_consumed: ", total_energy_consumed)
            heapq.heappush(available_processors, (task_arrival_time + task_duration, priority, proc_energy))
            break
    available_processors = sorted(available_processors)

print(total_energy_consumed)
