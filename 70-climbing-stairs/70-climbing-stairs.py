class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def process(rest):
            if rest == 0:
                return 1
            elif rest < 0:
                return 0
            return process(rest - 1) + process(rest - 2)
        
        return process(n)
    
      