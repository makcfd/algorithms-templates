"""длины слов «ноль», «один»
1 - один: длина слова 4 символа
"""

digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]


def number_strength(num):
    strength = digit_lengths[num]
    return strength


def insertion_sort_by_key(array, key):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and key(item_to_insert) < key(array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    print(array)


cards = [3, 7, 9, 2, 3]

insertion_sort_by_key(cards, number_strength)
