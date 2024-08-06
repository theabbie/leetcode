from collections import *

class Solution:
    def BFS(self, graph, i):
        q = deque([(i, self.price[i])])
        dist = {}
        dist[i] = self.price[i]
        while len(q) > 0:
            curr, d = q.pop()
            for j in graph[curr]:
                if dist.get(j, float('inf')) > d + self.price[j]:
                    dist[j] = d + self.price[j]
                    q.appendleft((j, d + self.price[j]))
        res = max(dist.keys(), key = lambda i: dist[i])
        return (res, dist)
    
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        self.price = price
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        x, dx = self.BFS(graph, 0)
        y, dy = self.BFS(graph, x)
        z, dz = self.BFS(graph, y)
        res = 0
        for i in range(n):
            cost = max(dy[i], dz[i])
            res = max(res, cost - price[i])
        return res