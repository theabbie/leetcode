class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            a, b = points[i]
            c, d = points[i + 1]
            x, y = abs(a - c), abs(b - d)
            res += max(x, y)
        return res