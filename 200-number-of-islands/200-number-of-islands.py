class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def bfs(x, y):
            
            q = deque([(x, y)])
            while q:
                row, col = q.popleft()
                for i in range(4):
                    a = row + dx[i]
                    b = col + dy[i]
                    
                    if 0 <= a < n and 0 <= b < m and grid[a][b] == "1":
                        grid[a][b] = "0"
                        q.append((a, b))
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    grid[i][j] = "0"
                    bfs(i, j)
                    ans += 1
        return ans
        
       
"""
TC: O(nm) | at most it will search each grid once
SC: O(min(M,N)) | because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,NM,N)
"""
       
                