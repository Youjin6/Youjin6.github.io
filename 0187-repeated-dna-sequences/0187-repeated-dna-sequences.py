class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        dic = defaultdict(lambda: 0)
        
        for i in range(len(s) - 9):
            string = s[i : i + 10]
            dic[string] += 1
            
        
        for val, times in dic.items():
            if times > 1:
                ans.append(val)
        
        return ans