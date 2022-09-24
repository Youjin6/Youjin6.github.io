class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        ans = []
        count = Counter(nums)
        for nums, times in count.items():
            bucket[times].append(nums)
        
        for i in reversed(bucket):

            for num in i:
                ans.append(num)
                if len(ans) == k:
                    return ans