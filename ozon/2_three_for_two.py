
def total_check(number_on_items: int, prices: list) -> int:
    freq_count = {}
    [freq_count.update({num: freq_count.get(num, 0) + 1}) for num in prices]

    return sum((v - v // 3) * int(k) for k, v in freq_count.items())


if __name__ == "__main__":
    iterations = int(input())
    for iter in range(iterations):
        number_on_items = int(input())
        prices = input().strip().split()
        print(total_check(number_on_items, prices))
