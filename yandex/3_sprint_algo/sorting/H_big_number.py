test = """5
86 88 39 58 96""".split("\n")


def input():
    return test.pop(0)


def is_element_stronger(element_1, element_2):
    if len(element_1) == len(element_2):
        return element_1 > element_2
    else:
        new_element_1 = element_1 + element_2
        new_element_2 = element_2 + element_1
        return new_element_1 > new_element_2


def insertion_sort(array, more):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and more(item_to_insert, array[j-1]):
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    print("".join(array))


if __name__ == "__main__":
    _ = int(input())
    array = [i for i in input().split()]
    insertion_sort(array, is_element_stronger)
