class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i == len(s)
            