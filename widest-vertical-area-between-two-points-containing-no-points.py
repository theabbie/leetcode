class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points = sorted(points)
        return max([points[i + 1][0] - points[i][0] for i in range(n - 1)])