class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        f = [[0 for _ in range(2)] for _ in range(n)]
        f[0][0] = 0
        f[0][1] = nums[0]
        
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1])
            f[i][1] = nums[i] + f[i - 1][0]
            
        
        return max(f[n - 1][0], f[n - 1][1])
        