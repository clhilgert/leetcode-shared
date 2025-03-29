class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        # track level 
        level = 0

        queue = deque([root])

        while queue:
            result.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                result[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1 

        return result
