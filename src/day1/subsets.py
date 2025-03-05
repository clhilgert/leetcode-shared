def subsets(nums):
    groups = []
    curr = []
    def helper(idx):
        # base case
        groups.append(curr[:])
        if idx >= len(nums):
            return
        for i in range(idx, len(nums)):
            curr.append(nums[i])
            helper(i + 1)
            curr.pop()
        # helper(i + 1)
            
    helper(0)
    return sorted(groups)
    
print(subsets([1,2,3]))