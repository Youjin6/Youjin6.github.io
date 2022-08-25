class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return

        # 逆向思维，判断跟边界连接的O，除了这些，剩下的全都为X

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        m = len(board)
        n = len(board[0])

        visited = [[0 for j in range(n)] for i in range(m)]


        def dfs(x, y):
            visited[x][y] = 1
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if next_x >= 0 and next_y >= 0 and next_x < m and next_y < n and board[next_x][next_y] == 'O' and visited[next_x][next_y] == 0:
                    dfs(next_x, next_y)

        for i in range(m):
            if board[i][0] == 'O' and visited[i][0] == 0:
                dfs(i, 0)
            if board[i][n-1] == 'O' and visited[i][n-1] == 0:
                dfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O' and visited[0][j] == 0:
                dfs(0, j)
            if board[m-1][j] == 'O' and visited[m-1][j] == 0:
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    board[i][j] = 'X'
