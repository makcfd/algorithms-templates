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
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                # get the word
                self.__child_words_for(current, words)
                return words
            current = current.children[char]
        self.__child_words_for(current, words)
        return words

    def __child_words_for(self, node, words):
        if node.is_word:
            words.append(node.text[::-1])
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)

n = int(input())
dictionary = [input().strip()[::-1] for _ in range(n)]

trie = PrefixTree()
for word in dictionary:
    trie.insert(word)
num_candidates = int(input())
for _ in range(num_candidates):
    suffix = input().strip()[::-1]

    print(*trie.starts_with(suffix))

