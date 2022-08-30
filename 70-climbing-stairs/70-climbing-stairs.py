class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def process(remain):
            if remain == 0:
                return 1
            elif remain < 0:
                return 0
            else:
                return process(remain - 1) + process(remain - 2)
    
        return process(n)
        
    

