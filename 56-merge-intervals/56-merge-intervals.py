class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        ans = []
        
        for a, b in intervals:
            if a <= end:
                end = max(end, b)
            
            else:
                ans.append([start, end])
                start = a
                end = b
        
        ans.append([start, end])
        return ans
            