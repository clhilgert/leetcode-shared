class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, num):
            if not node:
                return 0
            left = traverse(node.left, max(num, node.val))
            right = traverse(node.right, max(num, node.val))
            return left + right + int(node.val >= num)
        return traverse(root, float('-inf'))
