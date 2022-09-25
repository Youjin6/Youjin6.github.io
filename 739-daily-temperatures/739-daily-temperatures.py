class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        
        ans = [0] * n
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                front = stack.pop()
                ans[front] = i - front
            stack.append(i)
        
        while stack:
            front = stack.pop()
            ans[front] = 0
        
        return ans