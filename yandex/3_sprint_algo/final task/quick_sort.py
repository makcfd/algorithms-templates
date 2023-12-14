test = """5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80""".split("\n")


def input():
    global test
    return test.pop(0)


def is_first_better(element_1, element_2):
    if element_1[1] == element_2[1]:
        if element_1[2] == element_2[2]:
            return element_1[0] > element_2[0]
        else:
            return element_1[2] > element_2[2]
    return element_1[1] > element_2[1]


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = len(arr)//2
        left = 0
        right = len(arr) - 1
        while left <= pivot and right >= pivot:
            element_1 = arr[left]
            element_2 = arr[right]
            print(element_1, element_2)
            print(is_first_better(arr[left], arr[right]))
            if is_first_better(arr[left], arr[right]):
                #arr[left], arr[right] = arr[right], arr[left]
                pass
            else:
                arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right -= 1
        return arr

def main():
    data = []
    num_participants = int(input())
    for _ in range(num_participants):
        name, tasks, fines = input().strip().split()
        # data.append([int(i) if i.isdigit() else i for i in input().strip().split()])
        data.append([name, int(tasks), int(fines)*(-1)])
    #print(data)
    print(quicksort(data))


if __name__ == '__main__':
    main()
