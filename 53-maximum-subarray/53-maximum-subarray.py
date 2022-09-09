class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            if pre > 0:
                pre += nums[i]
            else:
                pre = nums[i]
            
            ans = max(pre, ans)
            
        
        return ans