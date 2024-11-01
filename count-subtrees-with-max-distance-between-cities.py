class Solution:
    def diameter(self, graph, root):
        n = len(graph)
        res = 0
        def d(i, p):
            nonlocal res
            s = 1
            a = b = 0
            mx = 0
            for j in graph[i]:
                if j == p:
                    continue
                h, cs = d(j, i)
                s += cs
                mx = max(mx, h)
                t, a, b = sorted([h, a, b])
            res = max(res, a + b)
            return mx + 1, s
        d, size = d(root, -1)
        return res, size
    
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        res = [0 for _ in range(n - 1)]
        for mask in range(1, 1 << n):
            graph = [[] for _ in range(n)]
            for u, v in edges:
                if mask & (1 << (u - 1)) and mask & (1 << (v - 1)):
                    graph[u - 1].append(v - 1)
                    graph[v - 1].append(u - 1)
            d, size = self.diameter(graph, min(i for i in range(n) if mask & (1 << i)))
            if d > 0 and size == mask.bit_count():
                res[d - 1] += 1
        return res