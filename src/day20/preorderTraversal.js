// https://leetcode.com/problems/binary-tree-preorder-traversal/description/

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/*
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function (root) {
  // if(!root)return []
  // return [root.val,...preorderTraversal(root.left),...preorderTraversal(root.right)]

  const output = [];

  function recursivehelper(root) {
    if (!root) return [];

    //current element val
    output.push(root.val);
    //recurse left side
    recursivehelper(root.left);
    //recurse right side
    recursivehelper(root.right);
  }

  recursivehelper(root);
  return output;
};
