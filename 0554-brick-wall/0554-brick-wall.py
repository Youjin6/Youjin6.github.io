class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = {}
        for row in wall:
            cur = 0
            for i in row:
                cur += i
                dic[cur] = dic.get(cur, 0) + 1
        
        length = sum(wall[0])
        max_val = 0
        for line, times in dic.items():
            if line == length:
                continue
            max_val = max(max_val, times)
                    
        return len(wall) - max_val