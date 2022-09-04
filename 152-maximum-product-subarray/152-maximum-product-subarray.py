class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            p1 = nums[i]
            p2 = nums[i] * max_product
            p3 = nums[i] * min_product
            
            cur_max = max(p1, max(p2, p3))
            cur_min = min(p1, min(p2, p3))
    
            ans = max(ans, cur_max)
            max_product = cur_max
            min_product = cur_min
            
        return ans