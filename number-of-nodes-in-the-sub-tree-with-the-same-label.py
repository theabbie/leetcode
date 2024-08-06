from collections import *
import bisect

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        nodes = [[0, 0] for _ in range(n)]
        tour = []
        pos = defaultdict(list)
        def dfs(i, prev):
            tour.append(i)
            pos[labels[i]].append(len(tour) - 1)
            nodes[i][0] = len(tour) - 1
            nodes[i][1] = 1
            for j in graph[i]:
                if j == prev:
                    continue
                dfs(j, i)
                nodes[i][1] += nodes[j][1]
        dfs(0, -1)
        res = []
        for i in range(n):
            res.append(bisect.bisect_right(pos[labels[i]], nodes[i][0] + nodes[i][1] - 1) - bisect.bisect_left(pos[labels[i]], nodes[i][0]))
        return res