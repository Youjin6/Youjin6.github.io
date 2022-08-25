class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not n:
            return -1
        m = len(grid[0])
        q = deque([])
        
        # iterate throught the grid and find a entry with value 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                    
        
        res = 0
        if q:
            res -=1
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while q:
            res += 1
            size = len(q)
            
            for j in range(size):
                front = q.popleft()
                for i in range(4):
                    a = front[0] + dx[i]
                    b = front[1] + dy[i]
                    if a in range(n) and b in range(m) and grid[a][b] == 1:
                        q.append((a, b))
                        grid[a][b] = 2
            
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return res
                    
                    
                    