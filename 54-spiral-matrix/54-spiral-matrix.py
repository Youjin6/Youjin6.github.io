class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        res = []
        if not matrix:
            return res
        
        n, m = len(matrix), len(matrix[0])
        visited = [[False] * m for _ in range(n)]
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        x, y, d = 0, 0, 0
                
        for i in range(n * m):
            res.append(matrix[x][y])
            visited[x][y] = True
            a = x + dx[d]
            b = y + dy[d]
            
            if a not in range(n) or b not in range(m) or visited[a][b]:
                d = (d + 1) % 4
                a = x + dx[d]
                b = y + dy[d]
            
            x = a
            y = b
            
        
        return res
        