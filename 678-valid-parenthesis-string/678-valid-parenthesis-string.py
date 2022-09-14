class Solution:
    def checkValidString(self, s: str) -> bool:
        lower = 0
        upper = 0
        
        for c in s:
            if c == '(':
                lower += 1
                upper += 1
            
            elif c == ')':
                lower -= 1
                upper -= 1
            
            else:
                lower -= 1
                upper += 1
                
            lower = max(0, lower)
            if lower > upper:
                return False
        
        if lower == 0:
            return True
        else:
            return False