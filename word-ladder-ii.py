from collections import defaultdict, deque

class Solution:
    def getPaths(self, parent, currpath, beginWord):
        if currpath[-1] == beginWord:
            self.paths.append(currpath[::-1])
            return
        for j in parent[currpath[-1]]:
            currpath.append(j)
            self.getPaths(parent, currpath, beginWord)
            currpath.pop()
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        n = len(beginWord)
        wordList = set(wordList + [beginWord])
        graph = defaultdict(list)
        for word in wordList:
            for i in range(n):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    currstr = word[0:i] + c + word[i+1:]
                    if currstr != word and currstr in wordList:
                        graph[word].append(currstr)
        dist = defaultdict(lambda: float('inf'))
        parent = defaultdict(list)
        dist[beginWord] = 0
        queue = deque([beginWord])
        while len(queue) > 0:
            curr = queue.pop()
            for j in graph[curr]:
                if dist[j] > dist[curr] + 1:
                    dist[j] = dist[curr] + 1
                    parent[j].clear()
                    parent[j].append(curr)
                    queue.appendleft(j)
                elif dist[j] == dist[curr] + 1:
                    parent[j].append(curr)
        self.paths = []
        self.getPaths(parent, [endWord], beginWord)
        return self.paths