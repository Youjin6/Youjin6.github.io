class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [None] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                t = stack.pop()
                ans[t] = i - t
            
            stack.append(i)
        
        while stack:
            t = stack.pop()
            ans[t] = 0
        
        return ans