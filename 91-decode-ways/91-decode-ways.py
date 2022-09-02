class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [None] * (len(s) + 1)
        
        
        def process(cur):
            # base case
            if cur == len(s):
                return 1
            # condition 
            if s[cur] == '0':
                return 0
            if memo[cur]:
                return memo[cur]
            # other case: single digit
            
            res = process(cur + 1)
            
            # other case: double digit
            if cur + 1 < len(s) and int(s[cur: cur + 2]) in range(1, 27):
                res += process(cur + 2)
            memo[cur] = res
            return res
        
        return process(0)
            