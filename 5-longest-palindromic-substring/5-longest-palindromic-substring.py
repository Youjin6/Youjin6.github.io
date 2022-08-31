class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        res = ''
        n = len(s)
        for i in range(len(s)):
            l, r = i - 1, i + 1
            while l in range(n) and r in range(n) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = s[l + 1: r]
            
            l, r = i, i + 1
            while l in range(n) and r in range(n) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = s[l + 1: r]
        return res
            