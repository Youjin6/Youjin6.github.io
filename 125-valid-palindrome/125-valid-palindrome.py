class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for i in s:
            if i.isalnum():
                ans.append(i.lower())
            
        return ans == ans[::-1]