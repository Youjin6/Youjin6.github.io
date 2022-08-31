class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        f = [0] * (n + 1) # include i
        g = [0] * (n + 1) # not include i 
        
        for i in range(1, n + 1):
            f[i] = nums[i - 1] + g[i - 1]
            g[i] = max(g[i - 1], f[i - 1])
        
        return max(f[n], g[n])
            