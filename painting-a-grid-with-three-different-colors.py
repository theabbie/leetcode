M = 10 ** 9 + 7

cache = {}

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        if m not in cache:
            good = []
            def gen(arr):
                if len(arr) == m:
                    good.append(arr[:])
                    return
                for l in range(3):
                    if arr and l == arr[-1]:
                        continue
                    arr.append(l)
                    gen(arr)
                    arr.pop()
            gen([])
            edges = [[] for _ in range(len(good))]
            g = len(good)
            for i in range(g):
                for j in range(g):
                    valid = True
                    for k in range(m):
                        if good[i][k] == good[j][k]:
                            valid = False
                            break
                    if valid:
                        edges[i].append(j)
            cache[m] = edges
        edges = cache[m]
        g = len(edges)
        dp = [1] * g
        ndp = [0] * g
        for _ in range(1, n):
            for i in range(g):
                ndp[i] = 0
                for j in edges[i]:
                    ndp[i] += dp[j]
                    ndp[i] %= M
            dp, ndp = ndp, dp
        return sum(dp) % M