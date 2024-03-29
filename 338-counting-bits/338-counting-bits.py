class Solution:
    def countBits(self, n: int) -> List[int]:
        f = [0] *(n + 1)
        
        for i in range(1, n + 1):
            f[i] = f[i >> 1] + (i & 1)
        
        return f