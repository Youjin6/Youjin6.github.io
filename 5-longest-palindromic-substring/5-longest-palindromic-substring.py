class Solution:
    def init(self, s):
        res = '#'
        for i in s:
            res += i
            res += '#'
        return res
    
    def longestPalindrome(self, s: str) -> str:
        string = self.init(s)    

        res = ''
        for i in range(len(string)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(string) and string[l] == string[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = string[l + 1: r]
        print(res)
        a = res.split('#')
        a = ''.join(a)
        return a
    