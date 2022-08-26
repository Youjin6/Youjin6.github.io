class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
    
        dic = defaultdict(list)
        ind = [0] * n
        
        for [course, pre] in prerequisites:
            dic[pre].append(course)
            ind[course] += 1
        
        q = deque([i for i in range(n) if ind[i] == 0])
        
        res = []
        while q:
            front = q.popleft()
            res.append(front)
            for i in dic[front]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        
        if len(res) == n:
            return res
        return []
            