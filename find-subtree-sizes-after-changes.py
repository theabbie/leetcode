from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        res = [0] * n
        graph = [[] for _ in range(n)]
        newgraph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[parent[i]].append(i)
        depths = defaultdict(list)
        def dfs(i, d, p):
            if len(depths[s[i]]) > 0:
                newgraph[depths[s[i]][-1]].append(i)
            elif p != -1:
                newgraph[p].append(i)
            depths[s[i]].append(i)
            for j in graph[i]:
                dfs(j, d + 1, i)
            depths[s[i]].pop()
        dfs(0, 0, -1)
        def sdfs(i):
            res[i] += 1
            for j in newgraph[i]:
                sdfs(j)
                res[i] += res[j]
        sdfs(0)
        return res