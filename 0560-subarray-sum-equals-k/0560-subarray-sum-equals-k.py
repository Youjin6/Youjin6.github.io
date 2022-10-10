class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        dic = defaultdict(lambda : 0)
        dic[0] = 1
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            
            res += dic[diff]
            dic[cur_sum] += 1
        
        return res