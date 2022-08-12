class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        visited = [False for _ in range(len(nums))]
        
        def dfs(u):
            if u == n:
                res.append(path[:])
                return 
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    dfs(u + 1)
                    visited[i] = False
                    path.pop()
        dfs(0)
        return res