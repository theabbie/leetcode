from collections import *

class Solution:
    def maxscore(self, graph, curr, prev, values, nonzero):
        key = (curr, prev, nonzero)
        if key in self.cache:
            return self.cache[key]
        take = values[curr]
        nottake = 0
        leaf = True
        for j in graph[curr]:
            if j != prev:
                leaf = False
                take += self.maxscore(graph, j, curr, values, nonzero)
                nottake += self.maxscore(graph, j, curr, values, True)
        if leaf and not nonzero:
            take = 0
        res = max(take, nottake)
        self.cache[key] = res
        return res
    
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        self.cache = {}
        return self.maxscore(graph, 0, -1, values, False)