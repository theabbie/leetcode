import bisect

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        points = []
        for l, r in intervals:
            bisect.insort(points, (l, 1))
            bisect.insort(points, (r + 1, -1))
        p = 0
        prev = None
        intervals = []
        for x, diff in points:
            p += diff
            if p == 0 and prev != None:
                if diff == 1:
                    intervals.append([prev, x])
                else:
                    intervals.append([prev, x - 1])
            if p == 1 and p - diff == 0:
                prev = x
        return intervals