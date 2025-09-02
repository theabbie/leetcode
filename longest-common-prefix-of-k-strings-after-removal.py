import heapq
from collections import *

class Trie:
    def __init__(self):
        self.c = {}
        self.pos = []
        
class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)
        trie = Trie()
        for i, s in enumerate(words):
            cur = trie
            cur.pos.append(i)
            for ch in s:
                if ch not in cur.c:
                    cur.c[ch] = Trie()
                cur = cur.c[ch]
                cur.pos.append(i)
        res = [0] * n
        queries = []
        def dfs(r, d):
            if d:
                prev = -1
                for j in r.pos + [n]:
                    if prev + 1 < j:
                        queries.append((prev + 1, j, d))
                    prev = j
            if len(r.pos) >= k + 1:
                for x in r.pos:
                    res[x] = max(res[x], d)
            for ch in r.c:
                if len(r.c[ch].pos) < k:
                    continue
                dfs(r.c[ch], d + 1)
        dfs(trie, 0)
        queries.sort(key=lambda x: x[0])
        heap = []
        p = 0
        for i in range(n):
            while p < len(queries) and queries[p][0] <= i:
                L, R, d = queries[p]
                heapq.heappush(heap, (-d, R))
                p += 1
            while heap and heap[0][1] <= i:
                heapq.heappop(heap)
            res[i] = max(res[i], -heap[0][0] if heap else 0)
        return res