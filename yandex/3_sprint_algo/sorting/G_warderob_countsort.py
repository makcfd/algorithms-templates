test = """2
2 1""".split('\n')


def input():
    return test.pop(0)


def sortColorsByCounting(arr):
    counts = [0, 0, 0]

    for color in arr:
        counts[color] += 1

    return [0] * counts[0] + [1] * counts[1] + [2] * counts[2]

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sortColorsByCounting(arr)
print(' '.join(map(str, sorted_arr)))
