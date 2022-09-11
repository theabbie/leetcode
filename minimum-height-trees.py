from collections import defaultdict, deque

class Solution:
    def BFS(self, graph, i):
        q = deque([(i, 0)])
        dist = {}
        dist[i] = 0
        while len(q) > 0:
            curr, d = q.pop()
            for j in graph[curr]:
                if dist.get(j, float('inf')) > d + 1:
                    dist[j] = d + 1
                    q.appendleft((j, d + 1))
        res = max(dist.keys(), key = lambda i: dist[i])
        return (res, dist)
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        x, dx = self.BFS(graph, 0)
        y, dy = self.BFS(graph, x)
        z, dz = self.BFS(graph, y)
        dist = [float('inf')] * n
        h = float('inf')
        for i in range(n):
            l = max(dy[i], dz[i])
            dist[i] = l
            h = min(h, l)
        return [i for i in range(n) if dist[i] == h]