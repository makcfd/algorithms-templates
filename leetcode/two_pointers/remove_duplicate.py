def removeDuplicates(nums):
    i = 1
    for idx in range(1,len(nums)):
        curr = nums[idx]
        prev = nums[idx-1]
        if curr != prev:
            nums[i] = nums[idx]
            i += 1
    return i


print(removeDuplicates([0,0,1,2,2,3,4]))
