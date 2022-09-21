# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # as a parent what do i need to calculate?
            # add up the  longest left child and right child
            ans = max(ans, left + right)
            
            # as a child what to return to my parent?
            # chose one side 
            return max(left, right) + 1
        
        ans = 0
        dfs(root)
        return ans
            
            