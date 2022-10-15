class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        if not n or not m:
            return []
        
        self.s = [[0] * (m + 1) for _ in range(n + 1)] 
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.s[i][j] = self.s[i - 1][j] + self.s[i][j - 1] - self.s[i - 1][j - 1] + matrix[i - 1][j - 1]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.s[row2][col2] - self.s[row2][col1 - 1] - self.s[row1 - 1][col2] + self.s[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)