class Solution:
    def strStr(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        for i in range(len(s)):
            if s[i : i + m] == t:
                return i
        
        return -1