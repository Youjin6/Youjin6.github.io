class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        n = len(s)
        i = n - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            res += 1
            i -= 1
        
        return res
            
            