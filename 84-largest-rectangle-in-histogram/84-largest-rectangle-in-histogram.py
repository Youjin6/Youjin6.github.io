class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        res = -1e8
        
        stack = []
        n = len(nums)
        
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                t = stack.pop()
                sub = i - stack[-1] - 1 if stack else i
                res = max(res, sub * nums[t])
            stack.append(i)
        while stack:
            t = stack.pop()
            sub = n - stack[-1] - 1 if stack else n
            res = max(res, sub * nums[t])
        
        return res