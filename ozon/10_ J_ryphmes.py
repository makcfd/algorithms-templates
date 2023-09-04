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

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.word = None

def insert(suffix, word, root):
    node = root
    for ch in suffix[::-1]:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
        node.count += 1
    node.word = word

def find_max_rhyme(suffix, root):
    node = root
    max_rhyme_node = None
    for ch in suffix[::-1]:
        if ch not in node.children:
            break
        node = node.children[ch]
        if node.count > 1:
            max_rhyme_node = node
    return max_rhyme_node.word if max_rhyme_node else None

n = int(input())
dictionary = [input().strip() for _ in range(n)]
root = TrieNode()
for word in dictionary:
    for i in range(len(word)):
        insert(word[i:], word, root)

q = int(input())
for _ in range(q):
    query = input().strip()
    print(find_max_rhyme(query, root))
