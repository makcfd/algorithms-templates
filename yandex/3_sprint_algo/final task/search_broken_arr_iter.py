# test = """9
# 5
# 19 21 100 101 1 4 5 7 12""".split("\n")


# def input():
#     global test
#     return test.pop(0)

def broken_search(nums, target) -> int:
    def find_pivot(nums, low, high):
        while low <= high:
            mid = (low + high) // 2
            if mid < high and nums[mid] > nums[mid + 1]:
                return mid
            if mid > low and nums[mid] < nums[mid - 1]:
                return mid - 1
            if nums[low] >= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def binary_search(nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    low = 0
    high = len(nums) - 1
    pivot = find_pivot(nums, 0, high)
    if pivot == -1:
        return binary_search(nums, low, high, target)
    if nums[pivot] == target:
        return pivot

    if nums[low] <= target <= nums[pivot - 1]:
        return binary_search(nums, low, pivot - 1, target)
    return binary_search(nums, pivot + 1, high, target)



def main():
    array_len = int(input())
    target = int(input())
    nums = [int(i) for i in input().strip().split()]
    print(broken_search(nums, target))


if __name__ == '__main__':
    main()