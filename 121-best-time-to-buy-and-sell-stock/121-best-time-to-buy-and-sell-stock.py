class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_val = float('inf')
        for i in range(len(prices)):
            min_val = min(min_val, prices[i])
            ans = max(ans, prices[i] - min_val)
        
        return ans