class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        
        # iterate each center
        for i in range(n):
            res += 1
            l = i - 1
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        for i in range(n):
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
