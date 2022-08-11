class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def dfs(index):
            if index == len(nums):
                ans.append(path.copy())
                return
            
            path.append(nums[index])
            dfs(index + 1)
            
            path.pop()
            dfs(index + 1)
            
        dfs(0)
        return ans