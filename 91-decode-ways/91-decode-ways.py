class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def process(cur):
            # base case
            if cur == len(s):
                return 1
            # condition 
            if s[cur] == '0':
                return 0
            
            # other case: single digit
            
            res = process(cur + 1)
            
            # other case: double digit
            if cur + 1 < len(s) and int(s[cur: cur + 2]) in range(1, 27):
                res += process(cur + 2)
            return res
        
        return process(0)
            