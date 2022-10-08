class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        res = ''
        for i in strs:
            min_len = min(len(i), min_len)
        
        
        for i in range(min_len):
            prefix = strs[0][i]
            same = True
            for j in range(len(strs)):
                if strs[j][i] != prefix:
                    same = False
            
            if same:
                res += prefix
            else:
                return res
        return res