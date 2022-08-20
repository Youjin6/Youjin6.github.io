class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        path = []
        ans = []
        
        def dfs(index, remain):
            if remain == 0:
                ans.append(path[:])
                return
            elif remain < 0 or index == n:
                return
            else:
                path.append(candidates[index])
                dfs(index, remain - candidates[index])
                path.pop()
                dfs(index + 1, remain)
        
        dfs(0, target)
        return ans
                