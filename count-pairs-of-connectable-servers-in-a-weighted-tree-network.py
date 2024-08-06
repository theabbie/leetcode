from collections import deque

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        res = [0] * n
        def dfs(i, prev, d, f):
            ctr = 0
            for j, w in graph[i]:
                if j == prev:
                    continue
                val = dfs(j, i, d + w, False)
                if f:
                    res[i] += val * ctr
                ctr += val
            if d % signalSpeed == 0:
                ctr += 1
            return ctr
        for i in range(n):
            dfs(i, -1, 0, True)
        return res