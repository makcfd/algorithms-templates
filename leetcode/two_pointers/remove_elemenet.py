# two pointetrs problem
# one pointer i use to iterate over the elements 
# second use for writing values that is not equal to val 
def removeElement(nums, val):
    i = 0
    for idx, num in enumerate(nums):
        if num != val:
            nums[i] = num
            i += 1
    nums[i:] = '_' * i
    return nums




nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
