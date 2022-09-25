class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        prev = float('-inf')
        ctr = 0
        for a, b in points:
            prev = min(prev, b + 1)
            if prev <= a:
                ctr += 1
                prev = b + 1
        return ctr