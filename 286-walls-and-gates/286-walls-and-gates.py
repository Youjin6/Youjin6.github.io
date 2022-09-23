class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n, m = len(rooms), len(rooms[0])
        queue = deque([])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        
        # add all the door the our queue
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
        
        # add grid to queue while queue is not empty
        d = 0
        while queue:
            x, y, d = queue.popleft()
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if a in range(n) and b in range(m):
                    if rooms[a][b] > d + 1:
                        rooms[a][b] = d + 1
                        queue.append((a, b, d + 1))
                    