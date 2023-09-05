test = """6
1 2 4 4 6 8
3""".split("\n")

test2 = """8
1 11 15 18 21 30 33 39
1""".split("\n")


def input():
    global test2
    return test2.pop(0)


def bin_search_first_day(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    # We check if the current value is equal to or greater than target and 
    # either it's the first element or the previous one is less than target. 
    # This helps us find the first occurrence.
    if arr[mid] >= target and (mid == 0 or arr[mid - 1] < target):
        return mid + 1
    elif arr[mid] < target:
        return bin_search_first_day(arr, mid + 1, right, target)
    else:
        return bin_search_first_day(arr, left, mid - 1, target)


def main():
    n = int(input().strip())
    savings = list(map(int, input().strip().split()))
    price = int(input().strip())

    one_bike_day = bin_search_first_day(savings, 0, n - 1, price)
    two_bike_day = bin_search_first_day(savings, 0, n - 1, 2 * price)

    print(one_bike_day, two_bike_day)

if __name__ == '__main__':
    main()
