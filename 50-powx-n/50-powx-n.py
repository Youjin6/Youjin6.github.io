class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        
        sign = 1
        if n < 0:
            sign = -1
        p = n * sign
        
        res = 1
        
        while p:
            if p & 1:
                res *= x
            
            x *= x
            p >>= 1
        
        return res if n > 0 else 1 / res