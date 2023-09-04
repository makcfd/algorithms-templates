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
                return None
            current = current.children[char]
        if current.is_word:
            return current

    def starts_with(self, prefix):
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                self.__child_words_for(current, words)
                return words
            # maybe make sense to access dict with get() method ? 
            current = current.children[char]
        self.__child_words_for(current, words)
        return words

    def __child_words_for(self, node, words):
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)


trie = PrefixTree()

trie.insert('apple')

print(*trie.starts_with('apc'))
