class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        count = {}
        ans = 0
        j = 0
        
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            while count[s[i]] > 1:
                count[s[j]] -= 1
                j += 1
            ans = max(ans, i - j + 1)
            
        
        return ans