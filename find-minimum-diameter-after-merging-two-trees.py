class Solution:
    def diameter(self, edges):
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        sizes = [0] * n
        def dfs(i, prev):
            sizes[i] = 1
            for j in graph[i]:
                if j != prev:
                    sizes[i] += dfs(j, i)
            return sizes[i]
        total = dfs(0, -1)
        def getcentroid(i, prev, total):
            for j in graph[i]:
                if j != prev and sizes[j] > total // 2:
                    return getcentroid(j, i, total)
            return i
        centroid = getcentroid(0, -1, total)
        def longest(i, prev):
            res = 1
            for j in graph[i]:
                if j != prev:
                    res = max(res, 1 + longest(j, i))
            return res
        a = b = 0
        for j in graph[centroid]:
            temp, a, b = sorted([a, b, longest(j, centroid)])
        return a + b
 
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        a = self.diameter(edges1)
        b = self.diameter(edges2)
        return max(a, b, (a + 1) // 2 + (b + 1) // 2 + 1)