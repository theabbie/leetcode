class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        res = 0
        def d(i, p):
            nonlocal res
            a = b = 0
            mx = 0
            for j in graph[i]:
                if j == p:
                    continue
                h = d(j, i)
                mx = max(mx, h)
                t, a, b = sorted([h, a, b])
            res = max(res, a + b)
            return mx + 1
        d(0, -1)
        return res