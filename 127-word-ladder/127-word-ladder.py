class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dist = collections.defaultdict(lambda :0)
        h = set(wordList)

        dist[beginWord] = 1

        queue = collections.deque()
        queue.append(beginWord)

        while queue:
            t = queue.popleft()

            for i in range(len(t)):
                for c in range(ord('a'), ord('z')+1):
                    cur_t = list(t)
                    c = chr(c)
                    cur_t[i] = c
                    cur_t = "".join(cur_t)

                    if cur_t in h and dist[cur_t] == 0:
                        dist[cur_t] = dist[t] + 1
                        if cur_t == endWord:
                            return dist[cur_t]

                        queue.append(cur_t)


        return 0
