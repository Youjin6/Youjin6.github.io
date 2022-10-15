class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            s.add(i)
                
        i = 1
        while True:
            if i not in s:
                return i
            i += 1
        
        return -1