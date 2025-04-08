/* 
https://leetcode.com/problems/combination-sum/description/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

*/

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  let result = [];
  const arr = [];
  let total = 0;

  backtrack(0);

  function backtrack(index) {
    // Base Case: when to end the search
    if (total > target) return;
    if (total === target) return result.push([...arr]);

    // Recursive case:
    // Loop through choices
    for (let i = index; i < candidates.length; i++) {
      // Prune the tree
      // Make choice
      arr.push(candidates[i]);
      total += candidates[i];
      // Backtrack (Unique | Repeat). If unique, use i+1. If repeat, use i
      backtrack(i);
      // Optional: End search early if found a solution
      // Undo choice
      arr.pop();
      total -= candidates[i];
    }
  }

  return result;
};

console.log(combinationSum([2, 3, 5], 8));
