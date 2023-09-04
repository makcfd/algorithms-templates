"""
6
2 1 3 1 1 4
"""


def check_efficiency(num_of_tasks: int, task_done: list):
    
    seen = set()
    efficient = "YES"
    for i in range(1, num_of_tasks):
        if task_done[i] in seen:
            efficient = "NO"
            break
        if task_done[i] != task_done[i-1]:
            seen.add(task_done[i-1])
    return efficient


if __name__ == "__main__":
    iterations = int(input())
    for iter in range(iterations):
        num_of_tasks = int(input())
        task_done = [int(i) for i in input().strip().split()]
        print(check_efficiency(num_of_tasks, task_done))
