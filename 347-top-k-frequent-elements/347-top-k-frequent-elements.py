class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        for num, times in counter.most_common(k):
            ans.append(num)
        
        return ans