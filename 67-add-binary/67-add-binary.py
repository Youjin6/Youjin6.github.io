class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a) - 1
        m = len(b) - 1
        carry = 0
        res = ''
        
        while n >= 0 or m >= 0:
            if n >= 0:
                carry += ord(a[n]) - ord('0')
                n -= 1
            if m >= 0:
                carry += ord(b[m]) - ord('0')
                m -= 1
            res = str(carry % 2) + res
            carry //= 2
        
        if carry:
            res = '1' + res
        return res