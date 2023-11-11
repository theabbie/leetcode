import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        times = [math.ceil(dist[i] / speed[i]) for i in range(n)]
        times.sort()
        res = 0
        while res < n and times[res] >= res + 1:
            res += 1
        return res