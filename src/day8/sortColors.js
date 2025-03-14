// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

// You must solve this problem without using the library's sort function.

// Example 1:

// red (0), white (1), blue (2)

// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

// Example 2:

// Input: nums = [2,0,1]
// Output: [0,1,2]

// Constraints:

//     n == nums.length
//     1 <= n <= 300
//     nums[i] is either 0, 1, or 2.

// [2,0,2,1,1,0]

function sortColors(nums) {
  let numbersCount = [0, 0, 0];
  // iterate through nums. count amount for each number
  nums.forEach((num) => {
    if (num === 0) {
      numbersCount[0]++;
    } else if (num === 1) {
      numbersCount[1]++;
    } else {
      numbersCount[2]++;
    }
  });

  // replace the amount of indexes assoicated with that number
  for (let i = 0; i < numbersCount[0]; i++) {
    nums[i] = 0;
  }
  for (let j = numbersCount[0]; j < numbersCount[1] + numbersCount[0]; j++) {
    nums[j] = 1;
  }
  for (
    let k = numbersCount[0] + numbersCount[1];
    k < numbersCount[0] + numbersCount[2] + numbersCount[1];
    k++
  ) {
    nums[k] = 2;
  }

  return nums;
}

console.log(sortColors([2, 0, 2, 1, 1, 0]));
