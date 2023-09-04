def plusOne(digits):
    num = 0
    for i, v in enumerate(digits[::-1]):
        num += 10**i*v
    return [int(i) for i in str(num+1)]

def test():
    assert plusOne([1,2,3]) == [1,2,4]
test()