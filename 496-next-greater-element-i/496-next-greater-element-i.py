class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = {}
        
        n = len(nums2)
        stack = []
        
        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                t = stack.pop()
                s[nums2[t]] = nums2[i]
            stack.append(i)
            
        while stack:
            t = stack.pop()
            s[nums2[t]] = -1
        print(s)
        ans = []
        for i in nums1:
            ans.append(s[i])
        
        return ans