class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        n -= 1
        while n:
            c = a + b
            a = b
            b = c
            n -= 1
        return b