class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        
        for i in range(len(s)):
            count[s[i]] = i
        
        res = []
        
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, count[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        
        return res