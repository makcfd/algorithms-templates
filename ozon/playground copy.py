word = 'decde'
word2 = 'id'

# films_1 = {'Форсаж', 'Достучаться до небес', 'Мстители: война бесконечности'}
# films_2 = {'Мстители: война бесконечности', 'Форсаж', 'Матрица'}
# films_3 = films_1.intersection(films_2)


# word_1_set = set(word)
# word_2_set = set(word2)
# match_values = len(word_1_set.intersection(word_2_set))
# print(match_values)
word = 'decide'
window_size = len(word2)
max_match_length = 0
for window_size in range(1, window_size+1):
    for i in range(len(word) - window_size + 1, -1, -1):
        print(word[i:i+window_size])
        if word[i:i+window_size] == word2[:window_size]:
            if window_size > max_match_length:
                max_match_length = window_size
        elif word[i:i+window_size] == word2[window_size:]:
            if window_size > max_match_length:
                max_match_length = window_size
print(max_match_length)

