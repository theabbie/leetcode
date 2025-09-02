class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0
        pmax = [float('-inf')] * (n + 1)
        prev = 0
        for i in range(n):
            curr = startTime[i] - prev
            prev = endTime[i]
            pmax[i + 1] = max(pmax[i], curr)
        smax = [float('-inf')] * (n + 1)
        prev = eventTime
        for i in range(n):
            curr = prev - endTime[n - i - 1]
            prev = startTime[n - i - 1]
            smax[i + 1] = max(smax[i], curr)
        res = max(res, pmax[n], smax[n])
        for i in range(n - 2):
            s = endTime[i + 1] - startTime[i + 1]
            rem = max(pmax[i + 1], smax[n - i - 2])
            if rem >= s:
                s = 0
            res = max(res, startTime[i + 2] - endTime[i] - s)
        first = endTime[0] - startTime[0]
        first = first if smax[n - 1] < first else 0
        last = endTime[-1] - startTime[-1]
        last = last if pmax[n - 1] < last else 0
        res = max(res, startTime[1] - first, eventTime - endTime[-2] - last)
        return res