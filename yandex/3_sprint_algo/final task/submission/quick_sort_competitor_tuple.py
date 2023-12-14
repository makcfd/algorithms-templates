"""
ID of package:
92507983
"""


class Competitor:
    """Класс для отображения участника."""

    def __init__(self, login: str, tasks: str, fines: str):
        self.login = login
        self.tasks = int(tasks)
        self.fines = int(fines)

    def __lt__(self, other):
        """
        Участник «меньше» (лучше) если у него больше решенных задач,
        при их равенстве лучше тот, у кого меньше штрафов, если и тут равенство,
        то «меньше» тот, у кого  логин идёт раньше в алфавитном
        (лексикографическом) порядке.
        """
        return (-self.tasks, self.fines, self.login) < (
            -other.tasks,
            other.fines,
            other.login,
        )

    def __str__(self):
        return self.login


def partition(arr: list, low: int, high: int):
    left_pointer = low - 1
    pivot = arr[high]

    for right_pointer in range(low, high):
        if arr[right_pointer] < pivot:
            left_pointer += 1
            arr[left_pointer], arr[right_pointer] = (
                arr[right_pointer],
                arr[left_pointer],
            )

    arr[left_pointer + 1], arr[high] = arr[high], arr[left_pointer + 1]
    return left_pointer + 1


def quicksort(arr: list, low: int, high: int):
    if low < high:
        partition_idx = partition(arr, low, high)
        quicksort(arr, low, partition_idx - 1)
        quicksort(arr, partition_idx + 1, high)


def main():
    num_participants = int(input())
    data = [Competitor(*input().strip().split()) for _ in range(num_participants)]
    quicksort(data, 0, len(data) - 1)
    print(*data, sep="\n")


if __name__ == "__main__":
    main()
