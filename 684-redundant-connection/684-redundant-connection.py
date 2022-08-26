class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(n + 1))
        
        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        
        def union(a, b):
            p[find(a)] = find(b)
            
            
        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        
        return []