class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = Counter(p)
        length_unique_char_in_p = len(dic)
        
        j = 0
        res = []
        count = 0
        
        for i in range(len(s)):
            dic[s[i]] -= 1
            if dic[s[i]] == 0:
                count += 1
            
            if i - j + 1 > len(p):
                if dic[s[j]] == 0:
                    count -= 1
                dic[s[j]] += 1
                j += 1
            
            if count == length_unique_char_in_p:
                res.append(j)
                
        return res
        
        