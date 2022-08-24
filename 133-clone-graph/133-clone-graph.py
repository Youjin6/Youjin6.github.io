"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        v = {}
        q = deque([node])
        v[node] = Node(node.val)
        
        while q:
            front = q.popleft()
            for nei in front.neighbors:
                if nei not in v:
                    q.append(nei)
                    v[nei] = Node(nei.val)
                v[front].neighbors.append(v[nei])
        
        return v[node]