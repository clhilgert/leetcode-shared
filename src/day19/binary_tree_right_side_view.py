class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        res = []
        def traverse(node, level):
            if not node: 
                return
            if level > len(res) - 1:
                res.append(node.val)
            else:
                res[level] = node.val
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        traverse(root, 0)
        return res
