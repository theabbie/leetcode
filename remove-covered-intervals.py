import bisect

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        points = []
        n = len(intervals)
        for i in range(n):
            a, b = intervals[i]
            bisect.insort(points, (a, a - b))
        i = 0
        while i < len(points):
            a, l = points[i]
            l = -l
            j = i + 1
            while j < len(points) and points[j][0] <= a + l:
                b, nl = points[j]
                nl = -nl
                if b + nl <= a + l:
                    points.pop(j)
                else:
                    j += 1
            i += 1
        return len(points)