class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        right = intervals[0][1]
        
        res = 1

        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:
                res += 1
                right = intervals[i][1]
        
        return len(intervals) - res