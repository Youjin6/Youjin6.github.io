class Solution:
    def climbStairs(self, n: int) -> int:
        record = [None] * (n + 1)
        record[0] = 1
        def process(remain):
            if record[remain]:
                return record[remain]
            elif remain < 0:
                return 0
            else:
                record[remain] =  process(remain - 1) + process(remain - 2)
                return record[remain]
        return process(n)
        
    

