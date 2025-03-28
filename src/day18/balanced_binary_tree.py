# https://leetcode.com/problems/balanced-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(root):
        is_balanced = True

        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            if abs(left - right) > 1:
                nonlocal is_balanced
                is_balanced = False
            return max(left + 1, right + 1)

        traverse(root)
        return is_balanced
