class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = [set() for _ in range(n)]
        for i in range(1, n):
            graph[parent[i]].add(i)
            graph[i].add(parent[i])
        sizes = [0] * n
        def dfs(i, prev):
            sizes[i] = 1
            for j in graph[i]:
                if j != prev:
                    sizes[i] += dfs(j, i)
            return sizes[i]
        def getcentroid(i, prev, total):
            for j in graph[i]:
                if j != prev and sizes[j] > total // 2:
                    return getcentroid(j, i, total)
            return i
        def longest(i, prev):
            res = 1
            for j in graph[i]:
                if j != prev and s[j] != s[i]:
                    res = max(res, 1 + longest(j, i))
            return res
        def solve(i):
            total = dfs(i, -1)
            centroid = getcentroid(i, -1, total)
            a = b = 0
            for j in graph[centroid]:
                if s[j] != s[centroid]:
                    temp, a, b = sorted([a, b, longest(j, centroid)])
            res = a + b + 1
            for j in list(graph[centroid]):
                graph[centroid].remove(j)
                graph[j].remove(centroid)
                res = max(res, solve(j))
            return res
        return solve(0)