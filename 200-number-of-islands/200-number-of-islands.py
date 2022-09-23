class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def dfs(x, y):
            grid[x][y] = '0'
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                
                if a in range(n) and b in range(m) and grid[a][b] == '1':
                    dfs(a, b)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        
        return ans
            