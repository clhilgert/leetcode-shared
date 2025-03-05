def subsets(nums):
    groups = []
    curr = []
    def helper(idx):
        # base case
        if idx >= len(nums):
            groups.append(curr[:])
            return
        curr.append(nums[idx])
        helper(idx + 1)
        curr.pop()
        helper(idx + 1)
            
    helper(0)
    return sorted(groups)
    
print(subsets([1,2,3]))