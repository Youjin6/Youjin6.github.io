class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)     
        if n < 3:
            return []
        
        # sort the nums
        nums.sort()
        
        def find(l, r, target, res):
            # l < r 做最外层
            while l < r:
                # 先判断相同
                if nums[l] + nums[r] == target:
                    res.append([-target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # 相同的情况下: i+1 = i: 去重 continue
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # right 也一样
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                # > target 右指针左移
                elif nums[l] + nums[r] > target:
                    r -= 1
                # < target 左指针右移
                else:
                    l += 1
                    
        for i in range(0, n - 2):
            # 注意要先判断 i 是否 > 0 访问 nums[i - 1]
            if i and nums[i] == nums[i - 1]:
                continue
            find(i + 1, n - 1, -nums[i], res)
        
        return res
    
"""
T: O(nlogn + n^2)    nlogn for sort, for each i, we iterate through the arary once
S: O(k)              where k is the number of results
"""