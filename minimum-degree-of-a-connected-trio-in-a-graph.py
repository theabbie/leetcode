class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        nb = [set() for _ in range(n)]
        B = 30
        d = [0] * n
        for u, v in edges:
            u -= 1
            v -= 1
            d[u] += 1
            d[v] += 1
            nb[u].add(v)
            nb[v].add(u)
        bigs = {i for i in range(n) if d[i] >= B}
        bigpairs = {}
        for i in bigs:
            for j in bigs:
                curr = float('inf')
                x = nb[i]
                y = nb[j]
                if len(x) > len(y):
                    x, y = y, x
                for k in x:
                    if k in y:
                        curr = min(curr, d[k])
                bigpairs[(i, j)] = min(bigpairs.get((i, j), float('inf')), curr)
        res = float('inf')
        for i in sorted(range(n), key = lambda x: d[x]):
            for j in nb[i]:
                if d[i] >= B and d[j] >= B:
                    res = min(res, d[i] + d[j] + bigpairs[(i, j)] - 6)
                    continue
                if d[i] + d[j] - 6 >= res:
                    continue
                x = nb[i]
                y = nb[j]
                if len(x) > len(y):
                    x, y = y, x
                for k in x:
                    if k in y:
                        res = min(res, d[i] + d[j] + d[k] - 6)
        if res == float('inf'):
            return -1
        return res