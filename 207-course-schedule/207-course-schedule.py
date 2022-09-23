class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        queue = deque([])
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            dic[pre].append(course)
            indegree[course] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = 0
        while queue:
            front = queue.popleft()
            res += 1
            for i in dic[front]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return res == numCourses
            
        
        