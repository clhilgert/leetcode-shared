/* 
https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  let res = [[]];

  for (let i = 0; i < nums.length; i += 1) {
    let addRes = res.map((x) => [...x]);

    for (let j = 0; j < addRes.length; j += 1) {
      addRes[j].push(nums[i]);
    }
    res = [...res, ...addRes];
  }
  return res;
};

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  const result = [];
  const arr = [];
  backtrack(0);
  return result;

  function backtrack(startIndex) {
    // Update result at each node:
    result.push([...arr]);
    // Base case: reach the end of nums arr:
    if (startIndex === nums.length) return;

    // Recursive case:
    // Loop through choices
    for (let i = 0; i < nums.length; i++) {
      // Prune the tree:
      if (i < startIndex) continue;
      // Make choice
      arr.push(nums[i]);
      // Backtrack (Unique | Repeat). If unique, use i+1. If repeat, use i
      backtrack(i + 1);
      // Optional: End search early if found a solution
      // Undo choice
      arr.pop();
    }
  }
};

// If there is dups, think about sorting
// For permutation, create a used arr

function backtrack() {
  // Base Case: when to end the search
  // Recursive case:
  // Loop through choices
  // Prune the tree
  // Make choice
  // Backtrack (Unique | Repeat). If unique, use i+1. If repeat, use i
  // Optional: End search early if found a solution
  // Undo choice
}
const nums = [1, 2, 3];

console.log(subsets(nums)); // Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
