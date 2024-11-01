class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        LOG = 18
        p = [[i] * LOG for i in range(n)]
        q = deque([(0, -1, 0)])
        depth = [0] * n
        order = []
        while q:
            curr, prev, d = q.pop()
            order.append((curr, prev))
            depth[curr] = d
            for j in graph[curr]:
                if j != prev:
                    p[j][0] = curr
                    q.appendleft((j, curr, d + 1))
        for l in range(1, LOG):
            for i in range(n):
                p[i][l] = p[p[i][l - 1]][l - 1]
        res = [0] * n
        for u, v in trips:
            res[u] += 1
            res[v] += 1
            if depth[u] > depth[v]:
                u, v = v, u
            ogu, ogv = u, v
            diff = depth[v] - depth[u]
            jump = 0
            while diff:
                if diff & 1:
                    v = p[v][jump]
                jump += 1
                diff //= 2
            for jump in range(LOG - 1, -1, -1):
                if p[u][jump] != p[v][jump]:
                    u = p[u][jump]
                    v = p[v][jump]
            LCA = p[u][0] if u != v else u
            res[LCA] -= 1
            if LCA != 0:
                res[p[LCA][0]] -= 1
        order.reverse()
        for i, prev in order:
            for j in graph[i]:
                if j != prev:
                    res[i] += res[j]
        @lru_cache(maxsize = None)
        def dp(i, p, pused):
            val = float('inf')
            if not pused:
                val = res[i] * (price[i] // 2) + sum(dp(j, i, True) for j in graph[i] if j != p)
            val = min(val, res[i] * price[i] + sum(dp(j, i, False) for j in graph[i] if j != p))
            return val
        return dp(0, -1, False)