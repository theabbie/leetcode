class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + endTime[i] - startTime[i]
        if k == n:
            return eventTime - p[n]
        res = max(res, startTime[k] - p[k], eventTime - endTime[-(k + 1)] - p[n] + p[n - k])
        for i in range(n - k - 1):
            total = startTime[i + k + 1] - endTime[i]
            used = p[i + k + 1] - p[i + 1]
            res = max(res, total - used)
        return res