# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def dfs(root):
            nonlocal ans
            if not root:
                ans += 'None#'
    
            else:
                ans += str(root.val)
                ans += '#'
            
                dfs(root.left)
                dfs(root.right)
        ans = ''
        dfs(root)
        
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs(l):
            if l[0] == 'None':
                l.pop(0)
                return
            
            root = TreeNode(l[0])
            l.pop(0)
            root.left = dfs(l)
            root.right = dfs(l)
        
            return root
        
        l = data.split('#')
        return dfs(l)
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))