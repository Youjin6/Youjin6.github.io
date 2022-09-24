class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(n + 1))
        print(p)
        
        def find(vertex):
            if p[vertex] != vertex:
                p[vertex] = find(p[vertex])
            return p[vertex]
        
        def union(v1, v2):
            p[find(v1)] = find(v2)
            
        
        for v1, v2 in edges:
            if find(v1) != find(v2):
                union(v1, v2)
            else:
                return [v1, v2]
        return []