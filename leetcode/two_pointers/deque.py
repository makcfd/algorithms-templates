from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

def levelOrder(root):
    if not root:
        return []
    queue = deque([root])
    results = []
    while queue:
        level = []
        for _ in range(len(queue)):
            element = queue.popleft()
            level.append(element.val)
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
        results.append(level)
    return results


if __name__ == '__main__':
    tree = deserialize('[3,9,20,null,null,15,7]')
    levelOrder(tree)
