class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = list(range(n))
        
        def find(node):
            if p[node] != node:
                p[node] = find(p[node])
            return p[node]
        
        def union(node1, node2):
            p[find(node1)] = find(node2)
        
        
        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
        
        ans = set()
        for n in p:
            ans.add(find(n))
        return len(ans)