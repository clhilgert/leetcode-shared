// https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

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
const maxDepth = function (root) {
  let queue = [];
  queue.push([root, 1]);
  let largestDepth = 1;
  while (queue.length) {
    let [element, depth] = queue.shift();
    largestDepth = Math.max(largestDepth, depth);
    if (element.left) queue.push([element.left, depth + 1]);
    if (element.right) queue.push([element.right, depth + 1]);
  }
  return largestDepth;
};
