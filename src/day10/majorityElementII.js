// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
 
// Example 1:

// Input: nums = [3,2,3]
// Output: [3]


// Example 2:
// Input: nums = [1]
// Output: [1]

// Example 3:
// Input: nums = [1,2]
// Output: [1,2]

// Example 4
// Input: nums = [1, 2, 3, 5, 6, 7] // 2
// Output: []
 
// example 5
// Input: 
const nums = [1, 1, 1, 2, 3, 3] // 2
// Output: []
const nums2 = [1, 1, 1, 2, 2, 2] // 2


// Constraints:

// 1 <= nums.length <= 5 * 104
// -109 <= nums[i] <= 109
 

// Follow up: Could you solve the problem in linear time and in O(1) space?
// Start time: 18:20


const majorityElement2 = (nums) => {
  const benchmark = Math.floor(nums.length / 3);
  const freqTracker = {};

  for (let i = 0; i < nums.length; i += 1){
    freqTracker[nums[i]] = freqTracker[nums[i]] + 1 || 1
  }

  const outputArray = [];

  for (let num in freqTracker) {
    if (freqTracker[num] > benchmark) outputArray.push(num)
  }

  return outputArray;
};

console.log(majorityElement2(nums))
console.log(majorityElement2(nums2))


/**
 * Given an array nums of size n, return the majority element.

  The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

  Example 1:

  Input: nums = [10,10,1,5,2,2, 2,2,2] // 9 // 5 majority, 4 non majority elements 
                           ^ 
  Output: 3
  Example 2:
    [1,2,3,5,10,10,10,10,10]


  nums = [10,10,1,5,       2,2,10,10,10]

  Input: nums = [2,2,1,1,1,2,2]
  Output: 2

 * 
 * 
 */

const majorityElement = (nums) => {
  let count = 0;
  let candidate = 0;

  nums.forEach((num)=>{
    if (count === 0) candidate = num;
    
    if (num === candidate) count += 1;
    else count -= 1
  })
}


  // def majorityElement(nums):
  //   count = 0
  //   candidate = 0
    
  //   for num in nums:
  //       if count == 0:
  //           candidate = num
        
  //       if num == candidate:
  //           count += 1
  //       else:
  //           count -= 1
    
  //   return candidate


  def majorityElement(self, nums: list[int]) -> list[int]:
        # Counters for the potential majority elements
        count1 = count2 = 0     
        # Potential majority element candidates
        candidate1 = candidate2 = 0

        # First pass to find potential majority elements.
        for num in nums:
            # If count1 is 0 and the current number is not equal to candidate2, update candidate1.
            if count1 == 0 and num != candidate2:
                count1 = 1
                candidate1 = num

            # If count2 is 0 and the current number is not equal to candidate1, update candidate2.
            elif count2 == 0 and num != candidate1:
                count2 = 1
                candidate2 = num
            
            # Update counts for candidate1 and candidate2.
            elif candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

            # If the current number is different from both candidates, decrement their counts.
            else:
                count1 -= 1
                count2 -= 1

        result = []
        threshold = len(nums) // 3  # Threshold for majority element

        # Second pass to count occurrences of the potential majority elements.
        count1 = count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

        # Check if the counts of potential majority elements are greater than n/3 and add them to the result.
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)

        return result