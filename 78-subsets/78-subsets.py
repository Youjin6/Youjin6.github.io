class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(u):
            if u == len(nums):
                ans.append(path[:])
                return
            
            path.append(nums[u])
            dfs(u + 1)
            path.pop()
            dfs(u + 1)
        dfs(0)
        return ans