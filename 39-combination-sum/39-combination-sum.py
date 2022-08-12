class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(u, remain):
            if remain == 0:
                ans.append(path[:])
            if remain < 0:
                return
            if u == len(c):
                return
            
            path.append(c[u])
            dfs(u, remain-c[u])
            
            path.pop()
            dfs(u + 1, remain)
        dfs(0, target)
        ans = [list(t) for t in set(tuple(_) for _ in ans)]
        return ans
        
            