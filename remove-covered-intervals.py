import bisect

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda p: (p[0], p[0] - p[1]))
        n = len(intervals)
        i = 0
        while i < len(intervals):
            a, b = intervals[i]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= b:
                c, d = intervals[j]
                if d <= b:
                    intervals.pop(j)
                else:
                    j += 1
            i += 1
        return len(intervals)