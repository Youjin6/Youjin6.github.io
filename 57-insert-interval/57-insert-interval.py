class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        k = 0
        n = len(intervals)
        
        while k < n and newInterval[0] > intervals[k][1]:
            res.append(intervals[k])
            k += 1
        
        while k < n and newInterval[1] >= intervals[k][0]:
            newInterval[0] = min(intervals[k][0], newInterval[0])
            newInterval[1] = max(intervals[k][1], newInterval[1])
            k += 1
            
        res.append(newInterval)
        while k < n:
            res.append(intervals[k])
            k += 1
        
        return res