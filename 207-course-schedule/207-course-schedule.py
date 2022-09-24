class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque([])
        for course, pre in prerequisites:
            dic[pre].append(course) 
            indegree[course] += 1
            
        # append the course indegree is 0 to queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        ans = 0
        while queue:
            front = queue.popleft()
            ans += 1
            for course in dic[front]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
                    
        return ans == numCourses
        