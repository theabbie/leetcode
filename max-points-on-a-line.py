class Solution:
    def isCollinear(self, a, b, c):
        mat = [[a[0] - b[0], b[0] - c[0]], [a[1] - b[1], b[1] - c[1]]]
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0] == 0
    
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        maxPoints = float('-inf')
        for i in range(n):
            for j in range(i + 1, n):
                a = points[i]
                b = points[j]
                currPoints = {tuple(a), tuple(b)}
                for x, y in points:
                    if x >= min(a[0], b[0]) and x <= max(a[0], b[0]) and y >= min(a[1], b[1]) and y <= max(a[1], b[1]):
                        if self.isCollinear(a, (x, y), b):
                            currPoints.add((x, y))
                maxPoints = max(maxPoints, len(currPoints))
        return max(maxPoints, 1)