class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [0] * (n + 1)
        dp[0] = startFuel
        for i in range(n):
            l, c = stations[i]
            for j in range(i, -1, -1):
                if dp[j] >= l:
                    dp[j + 1] = max(dp[j + 1], dp[j] + c)
        for i in range(n + 1):
            if dp[i] >= target:
                return i
        return -1