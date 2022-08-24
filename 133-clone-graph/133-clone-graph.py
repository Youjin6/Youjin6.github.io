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
        dic = {}
        
        def dfs(node):
            if node not in dic:
                dic[node] = Node(node.val)
                for nei in node.neighbors:
                    if nei not in dic:
                        dfs(nei)
        dfs(node)
        
        # copy the edges(neighbors)
        for k, v in dic.items():
            for nei in k.neighbors:
                v.neighbors.append(dic[nei])
        
        return dic[node]
        
        