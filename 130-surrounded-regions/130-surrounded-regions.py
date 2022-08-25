class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if not n:
            return [[]]
        m = len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def bfs(x, y):
            if visited[x][y] or board[x][y] != 'O':
                return
            visited[x][y] = True
            q = deque([(x, y)])
            while q:
                front = q.popleft()
                
                for i in range(4):
                    a = front[0] + dx[i]
                    b = front[1] + dy[i]
                    if a in range(n) and b in range(m) and board[a][b] == 'O' and not visited[a][b]:
                        visited[a][b] = True
                        q.append((a, b))
            
            
        # top, bottom
        for i in range(m):
            bfs(0, i)
            bfs(n - 1, i)
        
        # left, right
        for i in range(n):
            bfs(i, 0)
            bfs(i, m - 1)
            
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    board[i][j] = 'X'
        
        
            