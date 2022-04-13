import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        wordList = set(wordList + [beginWord])
        graph = {}
        for word in wordList:
            for i in range(n):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    curr = list(word)
                    curr[i] = c
                    currstr = "".join(curr)
                    if currstr != word and currstr in wordList:
                        graph[word] = graph.get(word, set()).union({currstr})
        heap = []
        deleted = {}
        dist = {}
        dist[beginWord] = 1
        for d in dist:
            heapq.heappush(heap, (dist[d], d))
        while len(heap) > 0:
            currdist, curr = heapq.heappop(heap)
            while (currdist, curr) in deleted and len(heap) > 0:
                deleted[(currdist, curr)] -= 1
                if deleted[(currdist, curr)] == 0:
                    del deleted[(currdist, curr)]
                currdist, curr = heapq.heappop(heap)
            for newcurr in graph.get(curr, []):
                if dist.get(newcurr, float('inf')) > 1 + currdist:
                    deleted[(currdist, curr)] = deleted.get((currdist, curr), 0) + 1
                    dist[newcurr] = 1 + currdist
                    heapq.heappush(heap, (1 + currdist, newcurr))
        return dist.get(endWord, 0)