test = """4
7 8
7 8
2 3
6 10""".split('\n')


def input():
    return test.pop(0)


def combine_intervals(array):
    array.sort(key=lambda x: (x[0], x[1]))
    result = []
    result.append(array[0])
    for i in range(1, len(array)):
        current_start, current_end = result[-1]
        new_start, new_end = array[i]
        if current_end >= new_start:
            result[-1] = [current_start, max(new_end, current_end)]
        else:
            result.append(array[i])

    return result


if __name__ == "__main__":
    number_of_intervals = int(input())
    intervals = []
    for interval in range(number_of_intervals):
        intervals.append([int(i) for i in input().strip().split()])
    result = combine_intervals(intervals)
    for item in result:
        print(*item)
