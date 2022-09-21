# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return True
        
        queue = deque([(p, q),])
        
        
        while queue:
            a, b = queue.popleft()
            if not check(a, b):
                return False
            if a:
                queue.append((a.left, b.left))
                queue.append((a.right, b.right))
        
        return True
        
        