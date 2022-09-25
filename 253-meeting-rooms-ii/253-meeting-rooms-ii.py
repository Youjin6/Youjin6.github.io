class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        heap = []
        heapq.heapify(heap)
        res = 0
        
        intervals.sort()
        for i in range(len(intervals)):
            while heap and intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i][1])
            res = max(res, len(heap))
            
        
        return res
                