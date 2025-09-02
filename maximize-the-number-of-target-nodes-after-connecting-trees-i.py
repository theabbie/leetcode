class Solution:
    def process(self, edges, k):
        n = 1 + len(edges)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(i, p, d):
            ctr = int(d <= k)
            for j in graph[i]:
                if j != p:
                    ctr += dfs(j, i, d + 1)
            return ctr
        return [dfs(i, -1, 0) for i in range(n)]
    
    def maxTargetNodes(self, edges1, edges2, k):
        fctr = self.process(edges1, k)
        sctr = max(self.process(edges2, k - 1))
        res = []
        n = len(edges1) + 1
        for i in range(n):
            res.append(fctr[i] + sctr)
        return res