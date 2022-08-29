class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dist = defaultdict(lambda: 0)
        # h = set(wordList)
        dist[beginWord] = 1
        
        queue = deque([beginWord])
        def get_next_word(word):
            next_words = []
            for i in range(len(word)):
                for c in range(ord('a'), ord('z') + 1):
                    new_word = list(word)
                    new_word[i] = chr(c)
                    new_word = ''.join(new_word)
                    next_words.append(new_word)
            return next_words
        
        while queue:
            t = queue.popleft()
            for next_word in get_next_word(t):
                if next_word in wordList and dist[next_word] == 0:
                    dist[next_word] = dist[t] + 1
                    queue.append(next_word)
        
        res = []
        path = [endWord]
        
        
        
        def dfs(t):
            if t == beginWord:
                res.append(path[::-1])
                
            else:
                for next_word in get_next_word(t):    
                        
                    if dist[next_word] + 1 == dist[t]:
                        path.append(next_word)
                        dfs(next_word)
                        path.pop()
        if endWord not in dist:
            return []
        dfs(endWord)
        return res
                