# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

        def __repr__(self) -> str:
            return self.value


def solution(node, elem):
    idx = 0
    while node:
        if node.value == elem:
            return idx
        idx += 1
        node = node.next_item
    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node4")
    print(idx)
    assert idx == -1


if __name__ == '__main__':
    test()
