# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])
        
        while q:
            front = q.popleft()
            front.left, front.right = front.right, front.left

            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
        
        return root