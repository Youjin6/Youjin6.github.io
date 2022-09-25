class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [1e8] * (amount + 1) 
        
        # base case
        f[0] = 0
        
        for i in coins:
            for j in range(i, amount + 1):

                f[j] = min(f[j], f[j - i] + 1)
        
        res = f[amount]
        return -1 if res == 1e8 else res