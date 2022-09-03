class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        f = [[0] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(amount + 1):
                f[i][j] = f[i - 1][j]
                if j >= coins[i - 1]:
                    f[i][j] += f[i][j - coins[i - 1]]
        
        return f[n][amount]