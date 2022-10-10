class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        dic = defaultdict(lambda : 0)
        res = 0
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
            
        
        for i in range(0, n + 1):
            tar = prefix[i] - k
            res += dic[tar]
            dic[prefix[i]] += 1
        
        return res