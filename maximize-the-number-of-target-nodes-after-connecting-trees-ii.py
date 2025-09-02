class Solution:
    def process(self, edges):
        n = 1 + len(edges)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        odds = [False] * n
        def dfs(i, p, d):
            if d & 1:
                odds[i] = True
            curr = int(d % 2 == 0)
            for j in graph[i]:
                if j != p:
                    curr += dfs(j, i, d + 1)
            return curr
        x = dfs(0, -1, 0)
        return [n - x if odds[i] else x for i in range(n)]
    
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        mctr = max(self.process(edges2))
        return [ctr + mctr for ctr in self.process(edges1)]