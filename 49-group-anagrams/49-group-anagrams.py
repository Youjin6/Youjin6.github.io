class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            w = ''.join(sorted(word))
            dic[w].append(word)
        
        return dic.values()