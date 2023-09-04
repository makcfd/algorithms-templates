test = """4 7
3 2 6 4
1 3
2 5
3 7
4 10
5 5
6 100
9 2""".split('\n')

test_2 = """1 8
1000000
1 900000
300001 900000
600001 900000
900001 900000
1200001 900000
1500001 900000
1800001 900000
2100001 900000""".split('\n')

def input():
    global test_2
    return test_2.pop(0)


num_processors, num_tasks = map(int, input().split())
energy_consumptions = sorted((int(energy)) for energy in input().split())
tasks = [tuple(map(int, input().split())) for _ in range(num_tasks)]


def best_proc(task_time, available_processors):
    proc_candidates = []
    for proc, finish_time in available_processors.items():
        if finish_time <= task_time:
            proc_candidates.append(proc)
        # no proc available
    if not proc_candidates:
        return -1
    best_proc = min(proc_candidates)
    return best_proc


available_processors = {key: 0 for key in energy_consumptions}
total_energy_consumed = 0
for task_arrival_time, task_duration in tasks:
    proc = best_proc(task_arrival_time, available_processors)
    if proc == -1:
        print("skipped: ", task_arrival_time, task_duration)
        continue
    total_energy_consumed += proc * task_duration
    print("task_arrival_time, task duration:", task_arrival_time, task_duration)
    print("proc_energy: ", proc)
    print("energy consumption increment: ", proc * task_duration)
    print("total_energy_consumed: ", total_energy_consumed)
    available_processors[proc] = task_arrival_time + task_duration
    print("proc will be free at", available_processors[proc])
print(total_energy_consumed)
