class Solution:
    def isHappy(self, n: int) -> bool:
        def add(n):
            res = 0
            while n:
                res += (n % 10) ** 2
                n //= 10
            return res
        
        fast = add(n)
        slow = n
        
        while fast != slow:
            fast = add(add(fast))
            slow = add(slow)
        return fast == 1