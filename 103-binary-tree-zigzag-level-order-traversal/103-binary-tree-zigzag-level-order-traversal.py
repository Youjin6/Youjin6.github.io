# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        
        q = deque([root])
        k = 0
        
        while q:
            n = len(q)
            level = []
            for i in range(n):
                head = q.popleft()
                level.append(head.val)
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
            
            k += 1
            if k % 2:
                ans.append(level)
            else:
                ans.append(reversed(level))
                
        
        return ans
                    