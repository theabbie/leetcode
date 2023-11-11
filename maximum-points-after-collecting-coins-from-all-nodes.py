from collections import *

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        cache = {}
        def maxscore(curr, prev, reduced):
            reduced = min(reduced, 14)
            key = (curr, prev, reduced)
            if key in cache:
                return cache[key]
            a = coins[curr] // pow(2, reduced) - k
            b = coins[curr] // pow(2, reduced + 1)
            for j in graph[curr]:
                if j == prev:
                    continue
                a += maxscore(j, curr, reduced)
                b += maxscore(j, curr, reduced + 1)
            res = max(a, b)
            cache[key] = res
            return res
        return maxscore(0, -1, 0)