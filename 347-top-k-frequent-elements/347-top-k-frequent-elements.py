class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_arr = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        res = []
        
        for val, times in count.items():
            ans_arr[times].append(val)
        
        for i in reversed(ans_arr):
            for val in i:
                res.append(val)   
                if len(res) == k:
                    return res