class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        n = len(temp)
        ans = [None] * n
        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                t = stack.pop()
                ans[t] = i - t
            
            stack.append(i)
        
        while stack:
            t = stack.pop()
            ans[t] = 0
        
        return ans