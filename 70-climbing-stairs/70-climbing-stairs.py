class Solution:
    def climbStairs(self, n: int) -> int:
        dic = [None] * (n + 1)
        dic[0] = 1
        
        def process(rest):
            if rest < 0: return 0
            elif dic[rest]:
                return dic[rest]

            dic[rest] = process(rest - 1) + process(rest - 2)
            return dic[rest]
        
        return process(n)
    
      