from collections import *

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        def get(x):
            res = 0
            for _ in range(x - 1):
                res += time;
                if (res // change) % 2:
                    res = (res // change + 1) * change
            return res + time
        q = deque([0])
        dist = [float('inf')] * n
        steps = 0
        while q:
            if steps > dist[n - 1] + 1:
                break
            for _ in range(len(q)):
                i = q.pop()
                if steps == dist[i] or steps > dist[i] + 1:
                    continue
                dist[i] = min(dist[i], steps)
                if i == n - 1 and steps > dist[n - 1]:
                    return get(steps)
                for j in graph[i]:
                    q.appendleft(j)
            steps += 1
        return get(dist[n - 1] + 2)