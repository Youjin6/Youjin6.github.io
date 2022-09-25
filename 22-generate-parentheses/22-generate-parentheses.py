class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, seq):
            if l == n and r == n:
                ans.append(seq)
            if l < n:
                dfs(l + 1, r, seq + '(')
            if r < n and l > r:
                dfs(l, r + 1, seq + ')')
        
        ans = []
        dfs(0, 0, '')
        return ans