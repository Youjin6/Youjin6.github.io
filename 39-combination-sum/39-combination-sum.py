class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(remain, cur):
            if remain == 0:
                res.append(path[:])
                return
            elif remain < 0:
                return
            
            for i in range(cur, len(candidates)):
                path.append(candidates[i])
                dfs(remain - candidates[i], i)
                path.pop()
        
        dfs(target, 0)
        
        return res