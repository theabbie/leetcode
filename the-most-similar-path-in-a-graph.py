class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        @lru_cache(maxsize = None)
        def dp(i, pos):
            if pos >= len(targetPath):
                return 0
            cost = int(names[i] != targetPath[pos])
            res = float('inf')
            for j in graph[i]:
                res = min(res, cost + dp(j, pos + 1))
            return res
        start = min(range(n), key = lambda p: dp(p, 0))
        res = [start]
        for pos in range(1, len(targetPath)):
            curr = (float('inf'), -1)
            for j in graph[res[-1]]:
                curr = min(curr, (dp(j, pos), j))
            res.append(curr[1])
        return res