
# two pointer 
def moveZeroes(nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if (nums[j] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1




def test():
    moveZeroes([0,1,0,3,12])
    

test()