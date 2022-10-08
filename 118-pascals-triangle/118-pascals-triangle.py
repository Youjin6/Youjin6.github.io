class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            helper = [0] + res[-1] + [0]
            cur_row = []
            for j in range(len(res[-1]) + 1):
                cur_row.append(helper[j] + helper[j + 1])
            
            res.append(cur_row)
        
        return res