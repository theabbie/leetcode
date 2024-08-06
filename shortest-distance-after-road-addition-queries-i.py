class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = [[] for _ in range(n)]
        res = []
        for l, r in queries:
            edges[l].append(r)
            dp = [float('inf')] * n
            dp[n - 1] = 0
            for i in range(n - 2, -1, -1):
                dp[i] = min(dp[i], 1 + dp[i + 1])
                for r in edges[i]:
                    dp[i] = min(dp[i], 1 + dp[r])
            res.append(dp[0])
        return res