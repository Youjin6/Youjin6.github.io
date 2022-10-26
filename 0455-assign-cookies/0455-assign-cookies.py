class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        n, m = len(g), len(s)
        ans = 0
        
        child, greed = 0, 0
        while child < n and greed < m:
            while greed < m and s[greed] < g[child]:
                greed += 1
            if greed < m:
                greed += 1
                child += 1
                ans += 1
        
        return ans
        