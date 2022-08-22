class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        
        def dfs(u):
            if u == n:
                res.append(path[:])
                return
            
            path.append(nums[u])
            dfs(u + 1)
            path.pop()
            dfs(u + 1)
        
        dfs(0)
        return res
    