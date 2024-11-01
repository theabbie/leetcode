class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n
        ndp = [0] * n
        for day in range(k - 1, -1, -1):
            for city in range(n):
                ndp[city] = stayScore[day][city] + dp[city]
                for other in range(n):
                    ndp[city] = max(ndp[city], travelScore[city][other] + dp[other])
            dp, ndp = ndp, dp
        return max(dp)