# https://leetcode.com/problems/insert-into-a-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(node):
            if not node:
                return
            if val < node.val:
                if node.left:
                    dfs(node.left)
                else:
                    node.left = TreeNode(val)
                    return
            else:
                if node.right:
                    dfs(node.right)
                else:
                    node.right = TreeNode(val)
                    return

        dfs(root)
        return root
