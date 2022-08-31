class Solution:
    def longestPalindrome(self, s: str) -> str:

        
        n = len(s)
        if n < 2:
            return s
        longest = 1
        start = 0
        
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            
        for L in range(2, n + 1):
            # left
            for i in range(n):
                # j - i + 1 = len -> j = L + i - 1
                j = L + i - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                
                # j - i + 1 < 4
                else:
                    if j - i + 1 < 4:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    
                if dp[i][j] and j - i + 1 > longest:
                    start = i
                    longest = j - i + 1
        return s[start: start + longest]
        