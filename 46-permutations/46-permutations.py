class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)

        
        def dfs(cur):
            if cur == n:
                res.append(nums[:])
                return
            
            for i in range(cur, n):
                nums[i], nums[cur] = nums[cur], nums[i]
                dfs(cur + 1)
                nums[i], nums[cur] = nums[cur], nums[i]
        dfs(0)
        return res
                    