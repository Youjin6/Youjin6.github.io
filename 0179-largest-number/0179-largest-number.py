class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        
        for idx, val in enumerate(nums):
            nums[idx] = str(val)
        
        nums = sorted(nums, key=cmp_to_key(compare))
        ans = ''.join(nums)

        i = 0
        while i < len(ans) and ans[i] == '0':
            i += 1
        
        if i == len(ans):
            return '0'
        
        return ans