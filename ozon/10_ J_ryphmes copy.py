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
        self.word = None

def insert(root, word):
    node = root
    for char in reversed(word):
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.word = word

def find_longest_suffix(root, word):
    node = root
    for char in reversed(word):
        if char in node.children:
            node = node.children[char]
        else:
            break
    while not node.word:
        node = list(node.children.values())[0]  # take any child
    return node.word

n = int(input().strip())
root = TrieNode()
for _ in range(n):
    word = input().strip()
    insert(root, word)

q = int(input().strip())
for _ in range(q):
    ti = input().strip()
    rhyme = find_longest_suffix(root, ti)
    if rhyme == ti:  # if the returned word matches the given word, run the query again to get a different match
        rhyme = find_longest_suffix(root, ti[:-1])
    print(rhyme)

