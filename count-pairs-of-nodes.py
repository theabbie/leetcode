from collections import *
import bisect

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        res = []
        vals = [len(graph[i]) for i in range(n)]
        vals.sort()
        for q in queries:
            curr = 0
            for i in range(n):
                a = len(graph[i])
                curr += len(vals) - bisect.bisect_left(vals, q - a + 1)
                if a > q - a:
                    curr -= 1
                nb = Counter()
                for j in graph[i]:
                    nb[j] += 1
                for j in nb:
                    if a + len(graph[j]) > q:
                        curr -= 1
                    if a + len(graph[j]) - nb[j] > q:
                        curr += 1
            res.append(curr // 2)
        return res