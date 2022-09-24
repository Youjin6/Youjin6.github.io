class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        ans = []
        for word in strs:
            w = ''.join(sorted(word))
            dic[w].append(word)
        
        for group in dic.values():
            ans.append(group)
        
        return ans