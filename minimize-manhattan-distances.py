from sortedcontainers import SortedList

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        points = [(x + y, x - y) for x, y in points]
        points.sort()
        xs = SortedList([x for x, y in points])
        ys = SortedList([y for x, y in points])
        res = float('inf')
        for x, y in points:
            xs.remove(x)
            ys.remove(y)
            res = min(res, max(xs[-1] - xs[0], ys[-1] - ys[0]))
            xs.add(x)
            ys.add(y)
        return res