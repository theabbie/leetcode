from collections import deque
import heapq

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        def getshort(i):
            heap = [(0, i)]
            dist = [float('inf')] * n
            dist[i] = 0
            v = set()
            while len(heap) > 0:
                d, curr = heapq.heappop(heap)
                if curr in v:
                    continue
                v.add(curr)
                dist[curr] = min(dist[curr], d)
                for j, w in graph[curr]:
                    if j not in v and dist[j] > d + w:
                        dist[j] = d + w
                        heapq.heappush(heap, (d + w, j))
            return dist
        f = getshort(0)
        s = getshort(n - 1)
        print(f, s)
        return [(f[u] + s[v] + w == f[n - 1] or f[v] + s[u] + w == f[n - 1]) and f[n - 1] != float('inf') for u, v, w in edges]