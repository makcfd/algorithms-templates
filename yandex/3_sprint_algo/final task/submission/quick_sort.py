"""
ID of package:
92465391
"""


class Competitor:
    """Класс для отображения участника."""

    def __init__(self, login, tasks, fines):
        self.login = login
        self.tasks = tasks
        self.fines = fines

    def __lt__(self):
        """
        Участник «меньше» (лучше) если у него больше решенных задач,
        при их равенстве лучше тот, у кого меньше штрафов, если и тут равенство,
        то «меньше» тот, у кого  логин идёт раньше в алфавитном
        (лексикографическом) порядке.
        """

    def __str__(self):
        return self.login


def is_first_better(element_1: list, element_2: list):
    if element_1[1] == element_2[1]:
        if element_1[2] == element_2[2]:
            return element_1[0] < element_2[0]
        else:
            return element_1[2] < element_2[2]
    return element_1[1] > element_2[1]


def partition(arr: list, low: int, high: int):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if is_first_better(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr: list, low: int, high: int):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def main():
    data = []
    num_participants = int(input())
    for _ in range(num_participants):
        name, tasks, fines = input().strip().split()
        data.append([name, int(tasks), int(fines)])
    quicksort(data, 0, len(data) - 1)
    for participant in data:
        print(participant[0])


if __name__ == "__main__":
    main()
