// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// Example 1:
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

// Explanation:

// There is no string in strs that can be rearranged to form "bat".
// The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
// The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

// Example 2:
// Input: strs = [""]
// Output: [[""]]

// Example 3:
// Input: strs = ["a"]
// Output: [["a"]]

// Example 4:
// Input: strs = ["eat","tea","tan","ate","nat","bat", "than"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"], ["than"]]

const convertWord = (word) => {
    const convertedWord = word.split("").sort().join("")
    return convertedWord
}

console.log(convertWord("eat")) // expecting "aet"

const groupAnagrams = (strs) => {
    const auxObj = {}

    for (let i = 0; i < strs.length; i += 1){
        const convertedWord = convertWord(strs[i])
        if (Object.hasOwn(auxObj, convertedWord)) auxObj[convertedWord].push(strs[i])
        else auxObj[convertedWord] = [strs[i]]
    }

    const returnArray = [];

    for (const key in auxObj) {
        returnArray.push(auxObj[key])
    }

    return returnArray;
}

// Input: 
const strs1 = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

// Example 2:
// Input: 
const strs2 = [""]
// Output: [[""]]

// Example 3:
// Input: 
const strs3 = ["a"]
// Output: [["a"]]

// Example 4:
// Input: 
const strs4 = ["eat","tea","tan","ate","nat","bat", "than"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"], ["than"]]

console.log ({
    1: groupAnagrams(strs1),
    2: groupAnagrams(strs2),
    3: groupAnagrams(strs3),
    4: groupAnagrams(strs4)
})

// const nums = Array(10).fill(1)
// nums[0] = 'a'
// console.log(nums)


function productExceptSelf(nums) {
    const preProduct = Array(nums.length).fill(1)
    const postProduct = Array(nums.length).fill(1)

    for (let i = 1; i < nums.length; i += 1){
        preProduct[i] = preProduct[i - 1] * nums[i - 1]
    }

    for (let j = nums.length - 2; j >= 0; j -= 1){
        postProduct[j] = postProduct[j + 1] * nums[j + 1]
    }

    // console.log(preProduct, postProduct)
    return preProduct.map((elem, index) => elem * postProduct[index])
};

console.log(productExceptSelf([1,2,3,4])) // 