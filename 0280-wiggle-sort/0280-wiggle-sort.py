class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
        i = 1
        while i + 1 < len(nums):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
            
        
        
        