# def rotate(nums, k):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     for i in range(k):
#         nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
#     print(nums)

# def rotate(nums, k):
#         n = len(nums)
#         k %= n

#         start = count = 0
#         while count < n:
#             current, prev = start, nums[start]
#             while True:
#                 next_idx = (current + k) % n
#                 nums[next_idx], prev = prev, nums[next_idx]
#                 current = next_idx
#                 count += 1

#                 if start == current:
#                     break
#             start += 1

def rotate(nums, k) -> None:
    n = len(nums)
    a = [0] * n
    for i in range(n):
        idx_insert = (i + k) % n
        a[idx_insert] = nums[i]

    nums = a
    print(nums)

rotate([1,2,3,4,5], 2)
