
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

console.log(productExceptSelf([1,2,3,4]))