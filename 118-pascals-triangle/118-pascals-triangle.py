class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = []
        for i in range(0, n):
            cur_row = [0] * (i + 1)
            cur_row[0] = cur_row[i] = 1
            for j in range(1, i):
                cur_row[j] = res[i - 1][j - 1] + res[i - 1][j]
            
            res.append(cur_row)
            
        
        return res
            
        