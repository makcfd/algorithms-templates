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


def solution(node, idx):
    current_idx = 0
    head = node
    previous_node = node
    while node:
        if current_idx == idx and head is not node:
            previous_node.next_item = node.next_item
            node.next_item = None
        elif current_idx == idx and head is node:
            head = node.next_item
            node.next_item = None
        current_idx += 1
        previous_node = node
        node = node.next_item
    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    #new_head = solution(node0, 1)
    # assert new_head is node0
    # assert new_head.next_item is node2
    # assert new_head.next_item.next_item is node3
    # assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3
    #new_head2 = solution(node0, 3)
    # assert new_head2 is node0
    # assert new_head2.next_item is node1
    # assert new_head2.next_item.next_item is node2
    # assert new_head2.next_item.next_item.next_item is None
    # print(new_head2)
    # print(new_head2.next_item)
    # print(new_head2.next_item.next_item)
    # print(new_head2.next_item.next_item.next_item)
    new_head2 = solution(node0, 0)
    print(new_head2)
    print(new_head2.next_item)
    print(new_head2.next_item.next_item)
    print(new_head2.next_item.next_item.next_item)

if __name__ == '__main__':
    test()
