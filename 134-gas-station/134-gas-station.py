class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        i=0
        while i<n:#枚举起点
            left=0
            for j in range(0,n+1): # 检查能不能从i走j步
                k=(i+j)%n
                left+=gas[k]-cost[k]
                if left<0:
                    break
            if j==n: # 满足条件
                return i
            i=i+j+1 # 如果从i到不了起点,只能走j步，说明 i~j之间都不可能走通
        return -1
