"""
6
2 1 3 1 1 4
"""


def find_pair(devs: int, skills: list):
    developers = [(i + 1, skills[i]) for i in range(devs)]

    while developers:
        first_dev = developers[0]
        min_diff = float('inf')
        second_dev = None

        for i in range(1, len(developers)):
            diff = abs(first_dev[1] - developers[i][1])
            if diff < min_diff:
                min_diff = diff
                second_dev = developers[i]
        print(first_dev[0], second_dev[0])
        developers.remove(first_dev)
        developers.remove(second_dev)


if __name__ == "__main__":
    iterations = int(input())
    for iter in range(iterations):
        number_on_devs = int(input())
        skll_level = list(map(int, input().split()))
        find_pair(number_on_devs, skll_level)
        print()
