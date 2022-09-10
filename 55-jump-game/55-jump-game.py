class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far_most = 0
        for i in range(len(nums)):
            if far_most < i:
                return False
            far_most = max(far_most, i + nums[i])
        
        return True