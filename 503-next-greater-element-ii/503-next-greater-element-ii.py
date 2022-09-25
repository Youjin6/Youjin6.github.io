class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums[:-1])
        ans = [0] * len(nums)
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                front = stack.pop()
                ans[front] = nums[i]
            
            stack.append(i)
        
        while stack:
            front = stack.pop()
            ans[front] = -1
        
        return ans[:n]