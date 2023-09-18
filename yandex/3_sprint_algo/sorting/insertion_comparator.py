"""длины слов «ноль», «один»
1 - один: длина слова 4 символа
"""

digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]


def is_element_weaker(element_1, element_2):
    return digit_lengths[element_1] < digit_lengths[element_2]


def insertion_sort_by_comparator(array, comparator_is_less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and comparator_is_less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    print(array)


cards = [3, 7, 9, 2, 3]
insertion_sort_by_comparator(cards, is_element_weaker)
