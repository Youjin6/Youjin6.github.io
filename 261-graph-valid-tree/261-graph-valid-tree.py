class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        p = list(range(n))
        
        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        
        def union(x, y):
            p[find(y)] = find(x)
            
        
        for a, b in edges:
            if find(a) != find(b):
                union(a, b)
            else:
                return False
        
        ans = set()
        for i in p:
            ans.add(find(i))
        if len(ans) > 1:
            return False
        
        return True
        
        