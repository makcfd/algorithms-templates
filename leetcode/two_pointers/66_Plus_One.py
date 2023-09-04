def plusOne(digits):
    result = str(int("".join(str(digit) for digit in digits)) + 1)
    return [int(num) for num in result]





def test():
    assert plusOne([1,2,3]) == [1,2,4]
