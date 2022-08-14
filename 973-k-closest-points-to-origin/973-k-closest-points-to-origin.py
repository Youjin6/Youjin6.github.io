class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heap.append([x**2 + y**2, (x, y)])
        
        heapq.heapify(heap)
        
        ans = []
        while k:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans