class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        x *= sign
        
        res = 0
        while x:
            res = res * 10 + (x % 10)
            x //= 10
        
        return res * sign if res < 2**31 else 0