class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        wordList = set(wordList + [beginWord])
        graph = {}
        for word in wordList:
            for i in range(n):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    currstr = word[0:i] + c + word[i+1:]
                    if currstr != word and currstr in wordList:
                        if word in graph:
                            graph[word].append(currstr)
                        else:
                            graph[word] = [currstr]
        dist = {}
        dist[beginWord] = 1
        queue = [(beginWord, 1)]
        visited = set()
        i = 0
        while i < len(queue):
            curr, k = queue[i]
            for j in graph.get(curr, []):
                if j not in visited:
                    dist[j] = dist.get(curr, float('inf')) + 1
                    if j == endWord:
                        return k + 1
                    visited.add(j)
                    queue.append((j, k + 1))
            i += 1
        return 0