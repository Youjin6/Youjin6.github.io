class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n , m = len(a) - 1, len(b) - 1
        
        carry = 0
        ans = ''
        while n >= 0 or m >= 0:
            if n >= 0:
                carry += int(a[n])
                n -= 1
            if m >= 0:
                carry += int(b[m])
                m -= 1
            
            ans = str(carry % 2) + ans
            carry //= 2
        
        if carry:
            ans = '1' + ans
        return ans