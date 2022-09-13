class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        i = 0
        while i < n:
            remain = 0
            for j in range(n + 1):
                cur = (i + j) % n
                remain += gas[cur] - cost[cur]
                if remain < 0:
                    break
                
            if j == n:
                return i
            i = i + j + 1
        
        return -1