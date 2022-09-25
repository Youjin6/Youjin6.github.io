class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        
        for i in range(n):
            if newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            
            elif newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                ans += intervals[i:]
                return ans
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        ans.append(newInterval)
        return ans