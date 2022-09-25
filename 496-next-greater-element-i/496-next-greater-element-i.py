class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        stack = []
        ans = []
        next_greater = [0] * m
        
        for i in range(m):
            while stack and nums2[i] > nums2[stack[-1]]:
                front = stack.pop()
                next_greater[front] = nums2[i]
            
            stack.append(i)
        
        while stack:
            front = stack.pop()
            next_greater[front] = -1
        
        for i in nums1:
            ans.append(next_greater[nums2.index(i)])
        
        return ans