class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        ind = [0] * n
        
        for [course, pre] in prerequisites:
            dic[pre].append(course)
            ind[course] += 1
        
        q = deque([i for i in range(n) if ind[i] == 0])
        
        res = 0
        while q:
            res += 1
            front = q.popleft()
            for i in dic[front]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        
        return res == n
            