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
                for neighbor in node.neighbors:
                    if neighbor not in dic:
                        dfs(neighbor)
        
        dfs(node)
        
        for n in dic:
            for nei in n.neighbors:
                dic[n].neighbors.append(dic[nei])
                
        return dic[node]
        
    
    