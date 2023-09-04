def find_smaller(arr):
    smallest_idx = 0
    smallest = arr[smallest_idx]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_idx, smallest = i, arr[i]
    return smallest_idx


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smaller(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selection_sort([1, 9, 20, 2, 4, 5, 0, 22]))
