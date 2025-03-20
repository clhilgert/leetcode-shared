// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

// Example 1:
// Input: nums = [1,2,3,4,5,6,7], k = 3
// [1,2,3,4] [5,6,7]

// [1,2,3,4,5,6,7]
// 4
// [1,2,3,1,5,6,7]
// 7
// [1,2,3,1,5,6,4]

// Output: [5,6,7,1,2,3,4]

// Example 2:
// Input: nums = [1,2,3,4,5,6,7], k = 24
// Output: [5,6,7,1,2,3,4]

// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// Example 2:
// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]

// Explanation:
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]

function rotate(nums, k) {
  const remainderK = k % nums.length;

  const prefixArray = nums.slice(nums.length - remainderK, nums.length);
  const postfixArray = nums.slice(0, nums.length - remainderK);

  return [...prefixArray, ...postfixArray];
}

const nums = [1, 2, 3, 4, 5, 6, 7];
/*
k = 2
changesMade = 8
store = 3
index = 0
[1$,2,3$,4,5$,6,7$,8]
*/

console.log(rotate(nums, 0)); // same as nums
console.log(rotate(nums, 2));
console.log(rotate(nums, 4));
console.log(rotate(nums, 9)); // same as 2
