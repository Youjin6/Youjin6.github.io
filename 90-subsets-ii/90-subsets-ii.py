class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(u):
            if u == len(nums):
                ans.append(sorted(path[:]))
                return
            
            path.append(nums[u])
            dfs(u + 1)
            path.pop()
            dfs(u + 1)
        
        dfs(0)
        res = []
        while ans:
            sub = ans.pop()
            if sub not in res:
                res.append(sub)
        
        return res
            