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


nun_of_proc, num_of_task = map(int, input().split())
processors = list(map(int, input().split()))

tasks = []
for _num_task in range(num_of_task):
    tasks.append(tuple(map(int, input().split())))


def task_scheduler(nun_of_proc, num_of_task, processors, tasks):
    scheduler = {}
    for task in tasks:
        print(task)
        scheduler[task] = {}
        for proc in processors:
            


print(task_scheduler(nun_of_proc, num_of_task, processors, tasks))
