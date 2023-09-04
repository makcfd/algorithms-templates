input_data = """3
task
decide
id
1
id""".split('\n')

input_data2 = """3
task
decide
id
1
flask""".split('\n')

output_Data = """task
decide
id
task
decide
task""".split('\n')


def input():
    global input_data
    return input_data.pop(0)


def output():
    global output_Data
    return output_Data.pop(0)


class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True

    def find(self, word):
        '''
        Returns the TrieNode representing the given word if it exists
        and None otherwise.
        '''
        current = self.root
        for char in word:
            if char not in current.children:
                return current
            current = current.children[char]
        if current.is_word:
            return current

    def starts_with(self, prefix):
        current = self.root
        longest_word = ""
        for char in prefix:
            if char not in current.children:
                if len(current.text[::-1]) > len(longest_word):
                    longest_word = current.text[::-1]
                return longest_word
            current = current.children[char]
        longest_word = self.__child_words_for(current, longest_word)
        return longest_word

    def __child_words_for(self, node, longest_word):
        if node.is_word and len(node.text[::-1]) > len(longest_word):
            longest_word = node.text[::-1]
        for letter in node.children:
            longest_word = self.__child_words_for(node.children[letter], longest_word)
        return longest_word


n = int(input())
dictionary = [input().strip()[::-1] for _ in range(n)]

trie = PrefixTree()
for word in dictionary:
    trie.insert(word)
num_candidates = int(input())
for _ in range(num_candidates):
    suffix = input().strip()[::-1]
    print(*trie.starts_with(suffix))

