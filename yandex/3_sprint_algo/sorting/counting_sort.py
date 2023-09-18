test = """2
2 1""".split('\n')


def input():
    return test.pop(0)


def counting_sort(array, k):
    counted_values = [0] * (k+1)
    for value in array:
        counted_values[value] += 1
    index = 0
    for value in range(0, k):
        limit = counted_values[value]
        for _ in range(1, limit+1):
            array[index] = value
            index += 1
    return array


# if __name__ == "__main__":
#     num_of_elements = int(input())
#     elements = [int(i) for i in input().strip().split()]
#     print(*counting_sort(elements, num_of_elements))

print(counting_sort([0,2,1,2,0,0,1], 7))
