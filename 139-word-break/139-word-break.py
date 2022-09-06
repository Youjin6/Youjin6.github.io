class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ULL = 1 << 64
        P = 131
        h = {}
        for word in wordDict:
            t = 0
            for c in word:
                t = (t * P + ord(c)) % ULL
            h[t] = 1

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        s = ' ' + s
        for i in range(n):
            if f[i]:
                t = 0
                for j in range(i + 1, n + 1):
                    t = (t * P + ord(s[j])) % ULL
                    if t in h:
                        f[j] = True
        return f[n]