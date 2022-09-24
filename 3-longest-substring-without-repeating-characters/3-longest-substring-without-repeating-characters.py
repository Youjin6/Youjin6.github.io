class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        """
        last position i appear, dp[i - 1] + 1
        """
        if not s:
            return 0
        dic = [-1 for _ in range(256)]
        
        dic[ord(s[0])] = 0
        pre = 1
        res = 1
        for i in range(1, len(s)):
            p1 = i - dic[ord(s[i])]
            p2 = pre + 1
            pre = min(p1, p2)
            res = max(pre, res)
            dic[ord(s[i])] = i
            
        
        return res