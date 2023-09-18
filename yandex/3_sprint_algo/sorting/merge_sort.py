
def merge_sort(array):
    if len(array) == 1:
        return array

    left = merge_sort(array[0: len(array)//2])
    right = merge_sort(array[len(array)//2: len(array)])

    result = []

    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    while l < len(left):
        result.append(left[l])
        l += 1

    while r < len(right):
        result.append(right[r])
        r += 1

    return result


print(merge_sort([39, 28, 44, 4, 10, 83, 11]))
