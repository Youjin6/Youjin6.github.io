class Solution:
    def canFinish(self, numCourses: int, p: List[List[int]]) -> bool:
        edges = defaultdict(list)
        indegree = [0] * numCourses
        
        for info in p:
            edges[info[1]].append(info[0])
            indegree[info[0]] += 1
            
        q = deque([u for u in range(numCourses) if indegree[u] == 0])
        visited = 0
        
        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return visited == numCourses