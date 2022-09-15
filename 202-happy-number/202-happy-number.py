class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            res = 0
            while x:
                res += (x % 10) ** 2
                x //= 10
                
            return res
        
        fast = get_next(n)
        slow = n
        
        while fast != slow:
            fast = get_next(get_next(fast))
            slow = get_next(slow)
        
        return fast == 1