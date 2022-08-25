class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n, m = len(rooms), len(rooms[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        INF = 2147483647
        q = deque([])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        
        d = 0
        while q:
            x, y, d = q.popleft()
            
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if a in range(n) and b in range(m):
                    if rooms[a][b] > d + 1:
                        rooms[a][b] = d + 1
                        q.append((a, b, d + 1))
        
        
                        
                        
                        
                        
                    
        
                    