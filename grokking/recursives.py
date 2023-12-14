# sum of elements in the array
# def sum(arr):
#     if not arr:
#         return 0
#     return arr[0] + sum(arr[1:])

# arr = [1, 6, 3, 4, 5]


# print(sum(arr))

# array counter
# def counter(arr):
#     if not arr:
#         return 0
#     else:
#         return 1 + counter(arr[1:])


# print(counter(arr))

# max value in the list

# def get_max_simple(arr):
#     if len(arr) == 2:
#         return arr[0] if arr[0] > arr[1] else arr[1]
#     sub_max = get_max_simple(arr[1:])
#     return arr[0] if arr[0] > sub_max else sub_max


# print(get_max_simple(arr))

# binary search recursive

def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, high, target)


arr = [6, 7, 8, 9, 10]
low = 0
high = len(arr) - 1
print(binary_search_recursive(arr, low, high, 7))
