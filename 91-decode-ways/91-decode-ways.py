class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[n] = 1

        
        for i in reversed(range(n)):
            if s[i] != '0':
            
                res = dp[i + 1]
                if i + 1 < len(s) and int(s[i: i + 2]) in range(10, 27):
                    res += dp[i + 2]
            
                dp[i] = res
            
        return dp[0]