"""
Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is distinct.
"""

# Approach 1: Sorting
# Sort values and go for i and i+1 element to compare
# elementa that are neighbours


def check_for_duplicates_sort(nums):
    i = 0
    nums = sorted(nums)
    for j in range(1, len(nums)-1):
        if nums[i] != nums[j]:
            i += 1
        else:
            return True
    return False

# Approach 2: Dictionary (hashtable)


def check_for_duplicates_dict(nums):
    nums_chekc = {}
    for num in nums:
        if num in nums_chekc:
            return True
        nums_chekc[num] = 1
    return False

# Approach 3: Set length


def check_for_duplicates_set(nums):
    return True if len(set(nums)) < len(nums) else False


def test() -> None:
    assert check_for_duplicates_sort([1, 2, 3, 4]) is False
    assert check_for_duplicates_sort([1, 2, 3, 1]) is True

    assert check_for_duplicates_dict([1, 2, 3, 4]) is False
    assert check_for_duplicates_dict([1, 2, 3, 1]) is True

    assert check_for_duplicates_set([1, 2, 3, 4]) is False
    assert check_for_duplicates_set([1, 2, 3, 1]) is True
