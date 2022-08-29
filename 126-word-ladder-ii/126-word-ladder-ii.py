class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dist = collections.defaultdict(lambda :0)
        h = set(wordList)

        dist[beginWord] = 1

        queue = collections.deque()

        queue.append(beginWord)

        while queue:
            t = queue.popleft()

            for i in range(len(t)):  # 枚举第i位可能的变化
                for c in range(ord('a'), ord('z') + 1):
                    cur_t = list(t)
                    c = chr(c)
                    cur_t[i] = c
                    cur_t = "".join(cur_t)

                    if cur_t in h and dist[cur_t] == 0:
                        dist[cur_t] = dist[t] + 1
                        if cur_t == endWord:
                            break
                        queue.append(cur_t)

        res = []
        path = [endWord]

        def dfs(t):
            if t == beginWord:
                res.append(path[::-1][:])

            else:
                for i in range(len(t)):
                    for c in range(ord('a'), ord('z') + 1):
                        cur_t = list(t)
                        c = chr(c)
                        cur_t[i] = c
                        cur_t = "".join(cur_t)

                        if dist[cur_t] + 1 == dist[t]:
                            path.append(cur_t)
                            dfs(cur_t)
                            path.pop()

        dfs(endWord)
        return res
