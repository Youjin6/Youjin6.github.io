class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        dic = set()
        for i in range(len(s) - k + 1):
            dic.add(s[i : i + k])
        
        return len(dic) == 2 ** k