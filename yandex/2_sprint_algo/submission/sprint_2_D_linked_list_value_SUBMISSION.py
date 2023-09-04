def solution(node, elem):
    idx = 0
    while node:
        if node.value == elem:
            return idx
        idx += 1
        node = node.next_item
    return -1
