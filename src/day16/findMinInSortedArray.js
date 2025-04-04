// Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

// [4,5,6,7,0,1,2] if it was rotated 4 times.
// [0,1,2,4,5,6,7] if it was rotated 7 times.
// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

// Given the sorted rotated array nums of unique elements, return the minimum element of this array.

// You must write an algorithm that runs in O(log n) time.

// Example 1:
// Input: nums = [7,8,9,1,2,3,4,5,6]
// Output: 1
// Explanation: The original array was [1,2,3,4,5] rotated 3 times.
// Example 2:

// Input: nums = [4,5,6,7,0,1,2]
// Output: 0
// Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
// Example 3:

// Input: nums = [11,13,15,17]
// Output: 11
// Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

// first check for completely sorted array if so return first
// search for bigger or smaller side
// if bigger side go right
// if smaller side record answer and check left

function minElement(nums) {
  if (nums[nums.length - 1] > nums[0] || nums.length === 1) return num[0];

  let left = 0;
  let right = nums.length - 1;
  let res = None;

  while (left <= right) {
    let mid = Math.floor((right - left) / 2);
    if (nums[mid] > nums[left]) {
      left = mid + 1;
    } else {
      res = mid;
      right = mid - 1;
    }
  }
  return res;
}
