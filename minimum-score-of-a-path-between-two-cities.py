from collections import defaultdict

class Solution:
    def DFS(self, graph, i, v):
        for j, d in graph[i]:
            if j not in v:
                v.add(j)
                self.DFS(graph, j, v)
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        res = float('inf')
        graph = defaultdict(set)
        for a, b, d in roads:
            graph[a].add((b, d))
            graph[b].add((a, d))
        v = {1}
        self.DFS(graph, 1, v)
        for a, b, d in roads:
            if a in v and b in v:
                res = min(res, d)
        return res