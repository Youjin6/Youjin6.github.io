class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque([])
        ans = []
        
        for course, pre in prerequisites:
            dic[pre].append(course) 
            indegree[course] += 1
            
        # append the course indegree is 0 to queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        

        while queue:
            front = queue.popleft()
            ans.append(front)
            for course in dic[front]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
                    
        return ans if len(ans) == numCourses else []