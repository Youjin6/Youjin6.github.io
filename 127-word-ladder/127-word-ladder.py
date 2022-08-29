class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        s = set(wordList)
        distance = defaultdict(lambda: 0)
        q = deque([beginWord])
        distance[beginWord] = 1
        
        while q:
            word = q.popleft()
            for i in range(len(word)):
                for c in range(ord('a'), ord('z') + 1):
                    new_word = list(word)
                    new_word[i] = chr(c)
                    new_word = ''.join(new_word)
                    
                    if new_word in s and distance[new_word] == 0:
                        distance[new_word] = distance[word] + 1
                        
                        if new_word == endWord:
                            return distance[new_word]
                        q.append(new_word)
        return 0
