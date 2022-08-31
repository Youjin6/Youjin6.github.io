class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        
        for i in range(1, n + 1):
            f[i] = nums[i - 1] + g[i - 1]
            g[i] = max(f[i - 1], g[i - 1])
        
        return max(f[n], g[n])