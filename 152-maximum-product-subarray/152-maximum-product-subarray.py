class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            p1 = nums[i]
            p2 = nums[i] * max_product
            p3 = nums[i] * min_product
            
            max_product = max(p1, max(p2, p3))
            min_product = min(p1, min(p2, p3))
            
            ans = max(ans, max_product)
            
            
        return ans