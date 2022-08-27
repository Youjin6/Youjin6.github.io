class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = list(range(n))
        
        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        
        def union(a, b):
            pa = find(a)
            pb = find(b)

            p[pa] = pb
            
            
        for [node1, node2] in edges:
            union(node1, node2)
            
        ans = set()
        for i in p:
            ans.add(find(i))
        return len(ans)