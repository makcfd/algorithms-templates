# test = """9
# 5
# 19 21 100 101 1 4 5 7 12""".split("\n")


# def input():
#     global test
#     return test.pop(0)


def broken_search(nums, target) -> int:
    def find_pivot(nums, low, high):
        if high < low:
            return -1
        if high == low:
            return low

        mid = (low + high) // 2
        if mid < high and nums[mid] > nums[mid + 1]:
            return mid
        if mid > low and nums[mid] < nums[mid - 1]:
            return mid - 1
        if nums[low] >= nums[mid]:
            return find_pivot(nums, low, mid - 1)
        return find_pivot(nums, mid + 1, high)

    def binary_search(nums, low, high, target):
        if high < low:
            return -1
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return binary_search(nums, mid + 1, high, target)
        return binary_search(nums, low, mid - 1, target)

    low = 0
    high = len(nums) - 1
    pivot = find_pivot(nums, 0, high)
    # no pivot in the array
    if pivot == -1:
        return binary_search(nums, low, high, target)
    if nums[pivot] == target:
        return pivot

    if nums[low] <= target:
        return binary_search(nums, low, pivot - 1, target)
    return binary_search(nums, pivot + 1, high, target)


def main():
    array_len = int(input())
    target = int(input())
    nums = [int(i) for i in input().strip().split()]
    print(broken_search(nums, target))


if __name__ == '__main__':
    main()
