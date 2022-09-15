class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        
        n, m = len(matrix), len(matrix[0])
        
        dic_row = []
        dic_col = []
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dic_row.append(i)
                    dic_col.append(j)
        
        
        for row in dic_row:
            matrix[row] = [0] * m
        
        for col in dic_col:
            for row in range(n):
                matrix[row][col] = 0
        
            
                