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
        
        def dfs(x, y):
            if visited[x][y] or board[x][y] != 'O':
                return
            visited[x][y] = True
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if a in range(n) and b in range(m) and board[a][b] == 'O':
                    dfs(a, b)
            
            
        # top, bottom
        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)
        
        # left, right
        for i in range(n - 1):
            dfs(i, 0)
            dfs(i, m - 1)
            
        
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if not visited[i][j]:
                    board[i][j] = 'X'
        return board
        
        
            