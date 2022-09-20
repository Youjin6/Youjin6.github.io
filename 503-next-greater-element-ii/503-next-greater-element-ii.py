class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums[:n - 1])
        
        ans = [-1] * (2 * n - 1)
        stack = []
        
        for i in range(2 * n - 1):
            while stack and nums[i] > nums[stack[-1]]:
                t = stack.pop()
                ans[t] = nums[i]
            stack.append(i)
            
        while stack:
            t = stack.pop()
            ans[t] = -1
        
        return ans[:n]