class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        heap = []
        heapify(heap)
        res = 0
        for i in range(len(intervals)):
            while heap and heap[0] <= intervals[i][0]:
                heappop(heap)
            
            heappush(heap, intervals[i][1])
            res = max(res, len(heap))
        
        return res