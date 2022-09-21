# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(a, b):
            if not a and not b:
                return True
            elif not a or not b or a.val != b.val:
                return False
            else:
                return is_same(a.left, b.left) and is_same(a.right, b.right)
            
        
        if not root:
            return False
        return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)