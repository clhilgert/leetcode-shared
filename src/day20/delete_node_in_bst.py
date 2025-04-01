# https://leetcode.com/problems/delete-node-in-a-bst/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]: 
      
        def dfs(node, key):
            # base case
            if not node:
                return None
            
            if node.val != key:
                # continue traversing
                if key < node.val:
                    node.left = dfs(node.left, key)
                else:
                    node.right = dfs(node.right, key)
                return node
            # decide which of the children to promote
            if not node.left and not node.right:
                return None
            if node.right and node.left:
                # pick inorder iteratively
                # while node.left exists continue going node.left, pick node.right first
                cur = node.right
                while cur.left:
                    cur = cur.left
                node.val = cur.val
                node.right = dfs(node.right, node.val)
                return node
            if node.left:
                return node.left
            if node.right:
                return node.right
        return dfs(root, key)