class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in highways:
            graph[u].append((v, w))
            graph[v].append((u, w))
        @lru_cache(maxsize = None)
        def dp(i, used, rem):
            if rem == 0:
                return 0
            res = float('-inf')
            for j, w in graph[i]:
                if not used & (1 << j):
                    res = max(res, w + dp(j, used | (1 << j), rem - 1))
            return res
        res = max(dp(i, 1 << i, k) for i in range(n))
        if res == float('-inf'):
            res = -1
        return res