class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = []
        
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            
            
            # window expired
            if q[0] + k == i:
                q.pop(0)
            
            # add ans to res
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res