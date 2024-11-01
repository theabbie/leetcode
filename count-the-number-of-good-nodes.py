class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = 0
        sz = [0] * n
        def dfs(i, prevnode):
            nonlocal res
            sz[i] += 1
            prev = -1
            good = True
            for j in graph[i]:
                if j != prevnode:
                    dfs(j, i)
                    if prev != -1 and sz[j] != prev:
                        good = False
                    prev = sz[j]
                    sz[i] += sz[j]
            if good:
                res += 1
        dfs(0, -1)
        return res