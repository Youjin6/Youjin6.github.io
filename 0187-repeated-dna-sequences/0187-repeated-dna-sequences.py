class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, ans = set(), set()
        
        for i in range(len(s) - 9):
            string = s[i: i + 10]
            if string in seen:
                ans.add(string)
            seen.add(string)
        return list(ans)
            