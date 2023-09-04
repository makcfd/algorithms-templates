

# def sum_of_two(numbers: list) -> int:
#     return sum(int(i) for i in numbers)


# if __name__ == "__main__":
#     iterations = int(input())
#     for iter in range(iterations):
#         numbers = input().strip().split()
#         print(sum_of_two(numbers))
def sum_of_numbers(numbers: list) -> int:
    return sum(numbers)

if __name__ == "__main__":
    iterations = int(input())
    for _ in range(iterations):
        numbers = list(map(int, input().strip().split()))
        print(sum_of_numbers(numbers))
