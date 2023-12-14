test = """5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80""".split("\n")

test_2 = """5
alla 0 0
gena 0 0
gosha 0 0
rita 0 0
timofey 0 0""".split("\n")


def input():
    global test
    return test.pop(0)



def is_first_better(element_1, element_2):
    if element_1[1] == element_2[1]:
        if element_1[2] == element_2[2]:
            return element_1[0] < element_2[0]
        else:
            return element_1[2] < element_2[2]
    return element_1[1] > element_2[1]


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if is_first_better(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
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


if __name__ == '__main__':
    main()
