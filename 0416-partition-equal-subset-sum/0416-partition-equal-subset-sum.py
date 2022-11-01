class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        s //= 2
        
        f = [False] * (s + 1)
        f[0] = 1
        
        for i in nums:
            for j in reversed(range(i, s + 1)):
                f[j] = max(f[j], f[j - i])
        
        
        return f[s]