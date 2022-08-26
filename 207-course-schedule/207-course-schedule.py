class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        res = []
        valid = True
        visited = [0] * n
        
        for [course, pre] in prerequisites:
            dic[pre].append(course)
            
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for i in dic[u]:
                if visited[i] == 0:
                    dfs(i)
                elif visited[i] == 1:
                    valid = False
                    return
            visited[u] = 2
            res.append(u)
        
        for i in range(n):
            if valid and visited[i] == 0:
                dfs(i)
                if not valid:
                    return False
        
        return valid