class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[1e8] * (amount + 1) for _ in range(n + 1)]
        
        # base case
        f[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(amount + 1):
                f[i][j] = f[i - 1][j]
                if j >= coins[i - 1]:
                    f[i][j] = min(f[i][j], f[i][j - coins[i - 1]] + 1)
        
        res = f[n][amount]
        return -1 if res == 1e8 else res