from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        n = len(routes)
        pos = defaultdict(list)
        for i in range(n):
            m = len(routes[i])
            for j in range(m):
                pos[routes[i][j]].append(i)
                graph[(routes[i][j], i)].add((routes[i][(j + 1) % m], i, 0))
        for el in pos:
            m = len(pos[el])
            for i in range(m):
                for j in range(i + 1, m):
                    a = pos[el][i]
                    b = pos[el][j]
                    graph[(el, a)].add((el, b, 1))
                    graph[(el, b)].add((el, a, 1))
        q = deque()
        dist = defaultdict(lambda: float('inf'))
        res = float('inf')
        for i in pos[source]:
            dist[(source, i)] = 1
            q.append((1, source, i))
        while len(q) > 0:
            currdist, curr, x = q.pop()
            if curr == target:
                res = min(res, currdist)
            for j, y, w in graph[(curr, x)]:
                if dist[(j, y)] > currdist + w:
                    dist[(j, y)] = currdist + w
                    if w == 0:
                        q.append((currdist + w, j, y))
                    else:
                        q.appendleft((currdist + w, j, y))
        if res == float('inf'):
            return -1
        return res