class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        points = sorted([bottom - 1] + special + [top + 1])
        mgap = 0
        n = len(points)
        for i in range(n - 1):
            mgap = max(mgap, points[i+1] - points[i] - 1)
        return mgap