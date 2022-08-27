class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = list(range(n))
        print(p)
        
        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        
        def union(a, b):
            pa = find(a)
            pb = find(b)

            for i, v in enumerate(p):
                if v == pa:
                    p[i] = pb
            
            
        for [node1, node2] in edges:
            union(node1, node2)
            
        print(p)
        count = Counter(p)
        return len(count)