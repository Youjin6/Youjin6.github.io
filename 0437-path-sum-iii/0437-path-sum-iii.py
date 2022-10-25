# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, cur):
            nonlocal res
            
            if not root:
                return
            cur += root.val
            res += count[cur - targetSum]
            count[cur] += 1
            dfs(root.left, cur)
            dfs(root.right, cur)
            count[cur] -= 1
            
        count = defaultdict(int)
        res = 0
        count[0] += 1
        
        dfs(root, 0)
        return res