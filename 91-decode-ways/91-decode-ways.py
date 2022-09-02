class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def p(cur):
            if cur == len(s):
                return 1
            if s[cur] == '0':
                return 0
            
            res = p(cur + 1)
            
            if cur + 1 < len(s) and int(s[cur : cur + 2]) in range(1, 27):
                res += p(cur + 2)
        
            return res
    
        return p(0)