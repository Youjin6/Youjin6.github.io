class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        match = j = 0
        total = len(count)
        n = len(s)
        res = []
        for i in range(n):
            count[s[i]] -= 1
            if count[s[i]] == 0:
                match += 1

            if i - j + 1 > len(p):
                if count[s[j]] == 0:
                    match -= 1
                count[s[j]] += 1
                j += 1

            if match == total:
                res.append(j)
        return res
