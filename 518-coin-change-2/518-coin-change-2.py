class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        f = [0] * (amount + 1)
        f[0] = 1
        
        for i in coins:
            for j in range(i, amount + 1):
                f[j] += f[j - i]
        
        return f[-1]