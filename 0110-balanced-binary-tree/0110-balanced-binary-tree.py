# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            # as parent:
            ans = max(ans, abs(left - right))
            
            # as child
            return max(left, right) + 1
        
        ans = 0
        dfs(root)
        if ans > 1:
            return False
        return True