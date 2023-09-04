
def intersect(nums1, nums2):
    d = {}
    resultik = []
    for num in nums1:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    for num2 in nums2:
        if num2 in d and d[num2] > 0:
            resultik.append(num2)
            d[num2] -= 1
    print(resultik)

   # return [k for k, v in d.items() if v >=1]

def test():
    assert intersect([1,2,2,1],[2,2]) == [2,2]

