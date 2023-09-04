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
