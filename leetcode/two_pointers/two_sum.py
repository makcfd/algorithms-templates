def twoSum(numbers, target):
    for i in range(0, len(numbers)-1):
        num1 = numbers[i]
        for j in range(i+1, len(numbers)):
            num2 = numbers[j]
            if num2 == target - num1:
                return i+1, j+1


numbers = [1, 2, 3, 4, 4, 9, 56, 90]
target = 8

print(twoSum(numbers, target))
