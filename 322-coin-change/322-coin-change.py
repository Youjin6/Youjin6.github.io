class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[1e8] *(amount + 1) for _ in range(n + 1)]
        
        f[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(amount + 1):
                f[i][j] = f[i - 1][j]
                if j >= coins[i - 1]:
                    f[i][j] = min(f[i][j], f[i][j - coins[i - 1]] + 1) 
                    
        if f[-1][-1] == 1e8:
            return -1
        return f[-1][-1]
    
    
"""
class Solution {
    public int coinChange(int[] coins, int amount) {

        int l = coins.length;
        var dp = new int[l + 1][amount + 1];

        // 将第一行的所有元素设置为一个较大值，为了后续求Min。
        Arrays.fill(dp[0], amount + 1);

        for (int i = 1; i <= l; i++){
            for (int j = 1; j <= amount; j++){
                // 选择了第i件物品，并求在金额j范围内满足要求的最小数量。
                if (j - coins[i - 1] >= 0){
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1);
                } else {
                // 不选第i件物品。
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        // eg. coins = [2], amount = 3
        return dp[l][amount] > amount ? -1 : dp[l][amount];
    }
}


"""