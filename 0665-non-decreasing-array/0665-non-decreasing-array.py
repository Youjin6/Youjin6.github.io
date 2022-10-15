class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def check():
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
            
            return True
        if not nums or len(nums) == 1:
            return True
        
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                a = nums[i - 1]
                b = nums[i]
                nums[i - 1] = nums[i] = a
                if check():
                    return True
                nums[i] = nums[i - 1] = b
                return check()
        return True