"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            sub = []
            n = len(queue)
            for i in range(n):
                front = queue.popleft()
                sub.append(front.val)
                for child in front.children:
                    queue.append(child)
            
            ans.append(sub)
        
        return ans
            