class UnionFind:
    def __init__(self, grid):
        n, m = len(grid), len(grid[0])
        self.count = 0
        self.parent = [None] * (m * n)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.parent[m * i + j] = m * i + j
                    self.count += 1
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = px
            self.count -= 1
    def getCount(self):
        return self.count
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if not n or not m:
            return 0
        uf = UnionFind(grid)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                    
                        if x in range(n) and y in range(m) and grid[x][y] == "1":
                            uf.union(m * i + j, m * x + y)
        return uf.getCount()
                    
                    
                    
                    
                    
                    
                    