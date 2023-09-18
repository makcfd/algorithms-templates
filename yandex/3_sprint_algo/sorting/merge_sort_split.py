
def merge(array, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    left_array = array[left:left+n1]
    right_array = array[mid:mid+n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(array, begin, end):
    if begin < end - 1:
        mid = (begin + end) // 2
        merge_sort(array, begin, mid)
        merge_sort(array, mid, end)
        merge(array, begin, mid, end)


# # Пример использования:
# arr = [4, 5, 3, 0, 1, 2]
# merge_sort(arr, 0, 4)
# print(arr)
# # Вывод: [0, 3, 4, 5, 1, 2]

def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

if __name__ == '__main__':
    test()
