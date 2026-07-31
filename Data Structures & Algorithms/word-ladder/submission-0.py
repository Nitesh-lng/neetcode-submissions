from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
            
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in words:
                        words.remove(next_word)
                        queue.append((next_word, steps + 1))
                        
        return 0