def partition(array, pivot):
    left = [i for i in array if i < pivot]
    center = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]
    return left, center, right


def quick_sort(array):
    # base case for reqursion
    if len(array) < 2:
        return array
    else:
        pivot = (array[0] + array[len(array)//2] + array[len(array)-1]) / 3
        left, center, right = partition(array, pivot)
        return quick_sort(left) + center + quick_sort(right)


a = [1, 4, 9, 2, 10, 11]
print(quick_sort(a))
