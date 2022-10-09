class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicST, dicTS = {}, {}
        
        for a, b in zip(s, t):
            if (a in dicST and dicST[a] != b) or (b in dicTS and dicTS[b] != a) :
                return False
            dicST[a] = b
            dicTS[b] = a
        
        return True
        
    
        
