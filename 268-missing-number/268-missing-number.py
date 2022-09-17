class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums) * (len(nums) + 1) // 2
        print(s)
        return s - sum(nums)