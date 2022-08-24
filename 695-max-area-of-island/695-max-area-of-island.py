class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if not n: 
            return 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def bfs(x, y):
            q = deque([(x, y)])
            res = 1
            while q:
                front = q.popleft()
                for i in range(4):
                    a = front[0] + dx[i]
                    b = front[1] + dy[i]
                    if a in range(n) and b in range(m) and grid[a][b] == 1:
                        q.append((a, b))
                        grid[a][b] = 0
                        res += 1
            return res
                
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(ans,bfs(i, j))
        return ans