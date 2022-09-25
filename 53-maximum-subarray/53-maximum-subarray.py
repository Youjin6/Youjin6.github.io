class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        pre = nums[0]
        
        for i in range(1, len(nums)):
            if pre > 0 :
                pre += nums[i]
                
            else:
                pre = nums[i]
            res = max(pre, res)
        return res
        
            