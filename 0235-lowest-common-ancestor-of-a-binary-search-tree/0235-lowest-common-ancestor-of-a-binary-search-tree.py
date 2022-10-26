# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            q, p = p, q
        
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right,p, q)
        elif q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else: 
            return root