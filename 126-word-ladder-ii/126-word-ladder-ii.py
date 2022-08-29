class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dist = defaultdict(lambda: 0)
        # h = set(wordList)
        dist[beginWord] = 1
        
        queue = deque([beginWord])
        
        while queue:
            t = queue.popleft()
            
            for i in range(len(t)):
                for c in range(ord('a'), ord('z') + 1):
                    new_word = list(t)
                    new_word[i] = chr(c)
                    new_word = ''.join(new_word)
                    
                    if new_word in wordList and dist[new_word] == 0:
                        dist[new_word] = dist[t] + 1
                        # if new_word == endWord:
                        #     break
                        queue.append(new_word)
        
        res = []
        path = [endWord]
        
        def dfs(t):
            if t == beginWord:
                res.append(path[::-1][:])
                
            else:
                for i in range(len(t)):
                    for c in range(ord('a'), ord('z') + 1):
                        new_word = list(t)
                        new_word[i] = chr(c)
                        new_word = ''.join(new_word)     
                        
                        if dist[new_word] + 1 == dist[t]:
                            path.append(new_word)
                            dfs(new_word)
                            path.pop()
        dfs(endWord)
        return res
                