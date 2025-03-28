// https://leetcode.com/problems/diameter-of-binary-tree/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
const diameterOfBinaryTree = function (root) {
  let largestCount = 0;

  function treversing(node) {
    if (!node.left && !node.right) return 1;
    let leftDepth = traversing(node.left);
    let rightDepth = traversing(node.right);

    let count = leftDepth + rightDepth;
    let largestDepth = Math.max(leftDepth, rightDepth) + 1;

    largestCount = Math.max(largestCount, count);

    return largestDepth;
  }

  treversing(root);
};
