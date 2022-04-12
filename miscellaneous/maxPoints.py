class Solution:
    def maxPoints(self, points):
        n = len(points)
        maxPoints = float('-inf')
        done = set()
        for i in range(n):
            for j in range(i + 1, n):
                a = points[i]
                b = points[j]
                xdiff = a[0] - b[0]
                ydiff = a[1] - b[1]
                slope = ydiff / xdiff if xdiff != 0 else float('inf') if ydiff > 0 else float('-inf')
                yint = a[1] - slope * a[0]
                if (slope, yint) in done:
                    continue
                done.add((slope, yint))
                currPoints = 0
                for x, y in points:
                    if xdiff * (b[1] - y) == (b[0] - x) * ydiff:
                        currPoints += 1
                maxPoints = max(maxPoints, currPoints)
        maxPoints = max(maxPoints, 1)
        return maxPoints

print(Solution().maxPoints([[1,1],[2,2],[3,3]]))