class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot):
    
    def find_match(root):
        if not root:
            return root == subRoot
        if traverse(root, subRoot):
            return True
        left = find_match(root.left)
        right = find_match(root.right)
        return left or right
    
    def traverse(root1, root2):
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False
        left = traverse(root1.left, root2.left)
        right = traverse(root1.right, root2.right)
        return left and right
    
    return find_match(root)