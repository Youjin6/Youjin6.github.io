class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        queue = deque([])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        d = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while queue:
            x, y, d = queue.popleft()
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if a in range(n) and b in range(m) and grid[a][b] == 1:
                    grid[a][b] = 2
                    queue.append((a, b, d + 1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return d
                    