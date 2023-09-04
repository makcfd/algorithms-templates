test = """3
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
    global test
    return test.pop(0)

def longest_common_suffix(word_ask, word_dict):
    """
    Return the length of the longest common suffix between two words.
    """
    window_size = len(word_ask)
    max_match_length = 0
    for window_size in range(1, window_size+1):
        for i in range(len(word_dict) - window_size + 1, -1, -1):
            if word_dict[i:i+window_size] == word_ask[:window_size]:
                if window_size > max_match_length:
                    max_match_length = window_size
            elif word_dict[i:i+window_size] == word_ask[window_size:]:
                if window_size > max_match_length:
                    max_match_length = window_size

    return max_match_length

def find_best_rhyme(query, dictionary):
    """
    Return the word from the dictionary that has the longest common suffix with the query.
    """
    best_match = ""
    best_length = -1
    for word_from_dict in dictionary:
        if word_from_dict == query:
            continue
        lcs = longest_common_suffix(query, word_from_dict)
        if lcs > best_length:
            best_match = word_from_dict
            best_length = lcs
    return best_match

# Input
n = int(input().strip())
dictionary = [input().strip() for _ in range(n)]
q = int(input().strip())
queries = [input().strip() for _ in range(q)]

# Process and output
for query in queries:
    print(find_best_rhyme(query, dictionary))


