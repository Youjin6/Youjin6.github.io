class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0 : -1}
        prefix = 0
        
        for i, n in enumerate(nums):
            prefix += n
            remainder = prefix % k
            
            if remainder not in dic:
                dic[remainder] = i
            else:
                if i - dic[remainder] > 1:
                    return True
        
        return False