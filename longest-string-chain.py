from collections import defaultdict

class Solution:
    def longest(self, graph, w, longestCache):
        if w in longestCache:
            return longestCache[w]
        mlen = 1
        for succ in graph[w]:
            l = self.longest(graph, succ, longestCache)
            mlen = max(mlen, 1 + l)
        longestCache[w] = mlen
        return mlen
    
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        graph = defaultdict(list)
        words = set(words)
        for w in words:
            wlen = len(w)
            for c in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(wlen + 1):
                    s = w[:i] + c + w[i:]
                    if s in words:
                        graph[w].append(s)
        longestCache = {}
        mlen = 1
        for w in words:
            l = self.longest(graph, w, longestCache)
            mlen = max(mlen, l)
        return mlen