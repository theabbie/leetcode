import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        hour = round(100 * hour)
        def check(x):
            t = 0
            for i in range(n - 1):
                t += 100 * math.ceil(dist[i] / x)
            return t * x + 100 * dist[-1] <= hour * x
        beg = 1
        end = 10 ** 7
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            if check(mid):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res