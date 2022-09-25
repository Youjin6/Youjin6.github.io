class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        n = len(intervals)
        intervals.sort(key = lambda x: x[1])
        end = intervals[0][1]
        
        for i in range(1, n):
            if intervals[i][0] < end:
                return False
            end = intervals[i][1]
        
        
        return True
        