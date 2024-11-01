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
    
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        n = 1 + len(edges)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        x, dx = self.BFS(graph, 0)
        y, dy = self.BFS(graph, x)
        z, dz = self.BFS(graph, y)
        return [max([(x, dy), (y, dz)], key = lambda p: p[1][i])[0] for i in range(n)]