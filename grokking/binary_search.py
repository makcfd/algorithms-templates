
def binary_search(list, item):
    """Binary search works only on sorted arrays"""
    list = sorted(list)
    low = 0
    high = len(list) - 1
    counter = 0

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            counter += 1
            return mid, counter
        if guess > item:
            high = mid - 1
            counter += 1
        else:
            low = mid + 1
            counter += 1
    return -1, counter


my_list = [1, 3, 10, 7, 9, 8]
result = binary_search(my_list, 9)

print(f"item idx: {result[0]}, number of iterations ot find: {result[1]}")
