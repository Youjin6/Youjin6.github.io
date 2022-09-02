class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
#         @lru_cache
#         def dfs(cur, remain):
#             if cur == len(coins):
#                 return 1 if remain == 0 else 0 
#             i = 0
#             ans = 0
#             while i * coins[cur] <= remain:
#                 ans += dfs(cur + 1, remain - i * coins[cur])
#                 i += 1
            
#             return ans
        
        
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        dp[n][0] = 1
        
        for i in reversed(range(n)):
            for j in range(amount + 1):
                dp[i][j] = dp[i + 1][j]
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j - coins[i]]
        
        return dp[0][amount]