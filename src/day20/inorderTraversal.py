# https://leetcode.com/problems/binary-tree-right-side-view/

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node, level):
            if not node:
                return
            if len(result) < level:
                result.append(node.val)
            traverse(node.right, level + 1)
            traverse(node.left, level + 1)

        traverse(root, 1)

        return result

        # DFS
        # Maintain level
        # Each index of result list is first visited of the level
        # Traverse right first
