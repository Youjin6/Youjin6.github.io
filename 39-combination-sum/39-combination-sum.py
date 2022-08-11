class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i, total):
            if total == target:
                res.append(path.copy())
                return
            
            if i == len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            dfs(i, total + candidates[i])
            
            path.pop()
            dfs(i + 1, total)
            
        dfs(0, 0)
        return res