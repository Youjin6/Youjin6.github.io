class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res =[a[0] for a in counter.most_common(k)]
        return res
        
        