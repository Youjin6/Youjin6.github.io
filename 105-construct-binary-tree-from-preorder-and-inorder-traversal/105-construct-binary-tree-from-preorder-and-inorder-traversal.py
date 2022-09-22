# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        index_head = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: index_head + 1], inorder[: index_head])
        root.right = self.buildTree(preorder[index_head + 1:], inorder[index_head + 1 :])
        
        return root

    """
    pre: head left right: [3]  9   20 15 7
    in.: left head right: 9   [3]  15 20 7
    
    """