class Solution:
    def isHappy(self, n: int) -> bool:
        def get(x):
            res = 0
            while x:
                res += (x % 10) ** 2
                x //= 10
                
            return res
        
        fast = get(n)
        slow = n
        
        while fast != slow:
            fast = get(get(fast))
            slow = get(slow)
        
        return fast == 1