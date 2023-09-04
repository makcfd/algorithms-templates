"""
ID of package:
    89650602.

Description:
    Task: Is to find how fat each element of the given array from
          a 0 (zero) element present in the same array.
    Solution:
          Algorythm iterate from left to right and after that from
          right to left, "scanning" the array for 0 (zero) elements
          and saving the resulted distances in list result.
          On the backward iteration the algorythms starts from position
          n-2 because n-1 element, or last element in the array has no
          neighbor. Once it starts with n-2 it proceeds to next element
          to the left end of the original array.

Args:
    street (list of int): Array of numbers.
                          Guaranteed to have one 0 (zero) element.

Returns:
    result (list of int): Array of numbers representing distance
                          to the closets 0 (zero) element.
"""

from typing import List


def find_nearest_zeros(street: List[int]) -> List[int]:
    array_size = len(street)
    result = [array_size] * array_size

    for index, value in enumerate(street):
        if value == 0:
            result[index] = 0
        else:
            result[index] = result[index - 1] + 1

    for index in range(array_size - 2, -1, -1):
        if street[index] != 0:
            result[index] = min(result[index], result[index + 1] + 1)
    return result


def read_input() -> List[int]:
    _ = input()
    return [int(value) for value in input().strip().split()]


if __name__ == "__main__":
    print(" ".join(str(element)
                   for element in find_nearest_zeros(read_input())))
