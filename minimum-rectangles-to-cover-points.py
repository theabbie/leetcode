class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        prev = float('-inf')
        res = 0
        for x, y in points:
            if x > prev + w:
                res += 1
                prev = x
        return res