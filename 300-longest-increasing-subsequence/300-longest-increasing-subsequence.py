class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        def binary_search(val):
            l = 0
            r = len(sub) - 1
            ans = -1
            while l <= r:
                mid = l + (r - l >> 1)
                if sub[mid] >= val:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        
        for i in nums:
            ans = binary_search(i)
            if ans == -1:
                sub.append(i)
            else:
                sub[ans] = i
        
        return len(sub)
        
        