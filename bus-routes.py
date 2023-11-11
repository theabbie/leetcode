from collections import *

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        for s in range(len(routes)):
            m = len(routes[s])
            for i in range(m):
                a = (routes[s][i], s)
                b = (routes[s][(i + 1) % m], s)
                graph[a].add((b, 0))
                graph[a].add(((routes[s][i], -1), 0))
                graph[(routes[s][i], -1)].add((a, 1))
        q = deque([(source, -1, 0)])
        dist = defaultdict(lambda: float('inf'))
        dist[(source, -1, 0)] = 0
        while len(q) > 0:
            curr, s, d = q.pop()
            if curr == target and s != -1:
                return d
            for j, cost in graph[(curr, s)]:
                if dist[j] > d + cost:
                    dist[j] = d + cost
                    if cost == 0:
                        q.append((j[0], j[1], dist[j]))
                    else:
                        q.appendleft((j[0], j[1], dist[j]))
        return -1