class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        p = []
        n = len(nums)
        st = [False for _ in range(len(nums))]
        def dfs(u):
            if u == n:
                res.append(p[:])
                return
            for i in range(n):
                if not st[i]:
                    st[i] = True
                    p.append(nums[i])
                    dfs(u + 1)
                    st[i] = False
                    p.pop()
        dfs(0)
        return res
