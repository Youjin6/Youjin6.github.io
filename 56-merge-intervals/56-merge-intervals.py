class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        
        for a, b in intervals:
            if a <= end:
                end = max(b, end)
            
            else:
                res.append([start, end])
                start = a
                end = b
        
        res.append([start, end])
        return res

                
                
                
