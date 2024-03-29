class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [1e8] * (amount + 1)
        
        f[0] = 0
        
        for i in coins:
            for j in range(i, amount + 1):
                f[j] = min(f[j], f[j - i] + 1)
            
        if f[amount] == 1e8:
            return -1
        return f[amount]