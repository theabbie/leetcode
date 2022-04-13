class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        n = len(points)
        vals = [i for i in range(n) if points[i][0] == x or points[i][1] == y]
        if len(vals) == 0:
            return -1
        return min(vals, key = lambda j: abs(points[j][0] - x) + abs(points[j][1] - y))