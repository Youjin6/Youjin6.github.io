class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if farthest < i:
                return False
            farthest = max(farthest, i + nums[i])
            
        
        return True
    
    
    
"""
[2, 3, 1, 1, 4]
i = 0, 1,
farthest position: 2 -> 4. farthest = max(farthest, i + nums[i] )

"""