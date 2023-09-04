"""Given a non-empty array of integers nums, every element appears
twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity
and use only constant extra space.
"""
from collections import Counter


def get_only_one(nums):
    freq = Counter(nums)
    for num in nums:
        if freq[num] == 1:
            return freq[num]


def test():
    assert get_only_one([2, 2, 1]) == 1
    assert get_only_one([2, 2, 1, 1]) is None
