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
            if not node.left and node.val > val:
                node.left = TreeNode(val)
                return
            elif not node.right and node.val < val:
                node.right = TreeNode(val)
                return
            # go left <
            if node.val > val:
                dfs(node.left)
            # go right >
            if node.val < val:
                dfs(node.right)

        dfs(root)
        return root
