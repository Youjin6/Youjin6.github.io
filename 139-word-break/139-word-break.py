class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s = ' ' + s
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if f[j - 1] and s[j : i + 1] in wordDict:
                    f[i] = True
                    break
        
        return f[n]