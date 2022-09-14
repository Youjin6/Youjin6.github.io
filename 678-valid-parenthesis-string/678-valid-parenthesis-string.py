class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        
        for c in s:
            if c == '(':
                low += 1
                high += 1
            
            elif c == ')':
                low -= 1
                high -= 1
            
            else:
                low -= 1
                high += 1
            
            low = max(0, low)
            if low > high:
                return False
        
        if low == 0:
            return True
        else:
            return False