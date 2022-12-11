import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        times = []
        for i in range(n):
            times.append((startTime[i], endTime[i], profit[i]))
        times.sort()
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_left(times, (times[i][1], times[i][1], 0))
            dp[i] = max(dp[i], times[i][2] + dp[j])
            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]