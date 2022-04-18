import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)
        maxclosest = 0
        for h in houses:
            i = bisect.bisect_left(heaters, h)
            mindist = float('inf')
            if 0 <= i < n:
                mindist = min(mindist, abs(h - heaters[i]))
            if i < n - 1:
                mindist = min(mindist, abs(h - heaters[i + 1]))
            if i > 0:
                mindist = min(mindist, abs(h - heaters[i - 1]))
            maxclosest = max(maxclosest, mindist)
        return maxclosest