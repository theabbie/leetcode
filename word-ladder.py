from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        wordList = set(wordList + [beginWord])
        graph = defaultdict(list)
        for word in wordList:
            for i in range(n):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    currstr = word[0:i] + c + word[i+1:]
                    if currstr != word and currstr in wordList:
                        graph[word].append(currstr)
        queue = deque([(beginWord, 1)])
        visited = set()
        while len(queue) > 0:
            curr, k = queue.pop()
            for j in graph.get(curr, []):
                if j not in visited:
                    if j == endWord:
                        return k + 1
                    visited.add(j)
                    queue.appendleft((j, k + 1))
        return 0