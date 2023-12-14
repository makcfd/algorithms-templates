# test = """9
# 5
# 19 21 100 101 1 4 5 7 12""".split("\n")


# def input():
#     global test
#     return test.pop(0)

def broken_search(nums, target) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def main():
    array_len = int(input())
    target = int(input())
    nums = [int(i) for i in input().strip().split()]
    print(broken_search(nums, target))


if __name__ == '__main__':
    main()
