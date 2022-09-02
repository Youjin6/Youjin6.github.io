class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def dfs(cur):
            if cur == len(s):
                return 1
            if s[cur] == '0':
                return 0
            
            # other case
            res = dfs(cur + 1)
            if cur + 1 < len(s) and int(s[cur: cur + 2]) in range(10, 27):
                res += dfs(cur + 2)
            return res
        
        return dfs(0)