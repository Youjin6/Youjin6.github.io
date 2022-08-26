class Solution:
    """
    status: 0. NOT VISITED 1. WIP  2.DONE 
    """
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        dic = collections.defaultdict(list)
        visited = [0] * n
        res = []
        valid = True
        
        for [course, pre] in prerequisites:
            dic[course].append(pre)
            
        
        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for i in dic[u]:
                if visited[i] == 0:
                    dfs(i)
                    if not valid:
                        return
                elif visited[i] == 1:
                    valid = False
                    return
            visited[u] = 2
            res.append(u)
            
        
        for i in range(n):
            if valid and not visited[i]:
                dfs(i)
                
        
        return valid