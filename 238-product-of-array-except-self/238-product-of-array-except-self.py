class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1e8] * len(nums)
        pre = 1
        post = 1
        
        for i in range(len(nums)):
            ans[i] = pre
            pre *= nums[i]
        
        for i in reversed(range(len(nums))):
            ans[i] *= post
            post *= nums[i]
        
        return ans
        
        
        