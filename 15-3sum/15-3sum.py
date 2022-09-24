class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        if n < 3:
            return ans
        nums.sort()
        def find(l, r, target):
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append([-target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        
        
        for i in range(n):
            if i and nums[i] == nums[i - 1]:
                continue
            find(i + 1, n - 1, -nums[i])
            
        return ans