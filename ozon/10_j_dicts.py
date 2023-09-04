input_data = """3
task
decide
id
6
flask
code
void
forces
id
ask""".split('\n')

def input():
    global input_data
    return input_data.pop(0)
"""
потом когда вводились слова для поиска рифмы
также итерировал, например ask: ask as
смотрю в словарь и первый попавщийся и был с макс суффиксом
"""
def generate_suffix_dict(word):
    return {word[-i:]: word for i in range(2, len(word) + 1)}

n = int(input())
dictionary = [input().strip() for _ in range(n)]
list_suffixes = list()
for word in dictionary:
    list_suffixes.append(generate_suffix_dict(word))
results = []
num_candidates = int(input())
for _ in range(num_candidates):
    query = input().strip()
    split_query = [query[-i:] for i in range(2, len(query) + 1)]
    for piece in split_query:
        for word_keys in list_suffixes:
            if piece in word_keys:
                results.append(word_keys[piece])
print(results)


# ...потом когда вводились слова для поиска рифмы
# также итерировал, например ask: ask as 
# смотрю в словарь и первый попавщийся и был с макс суффиксом

# оч колхозно (как по мне), но сработало
