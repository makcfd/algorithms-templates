test = """6
1 2 4 4 6 8
3""".split("\n")

test2 = """6
1 2 4 4 4 4
3""".split("\n")


def input():
    global test2
    return test2.pop(0)

def bin_search(arr, value):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
            
    return left if left < len(arr) and arr[left] >= value else -1

def find_bike_days(n, savings, s):
    day_one = bin_search(savings, s)
    day_two = bin_search(savings, 2*s)
    
    return day_one + 1, day_two + 1  # +1 так как отсчет дней начинается с 1, а не с 0

n = 6
savings = [1, 2, 4, 4, 6, 8]
s = 3
print(find_bike_days(n, savings, s))
