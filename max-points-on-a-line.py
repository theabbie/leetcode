class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        maxPoints = float('-inf')
        for i in range(n):
            for j in range(i + 1, n):
                a = points[i]
                b = points[j]
                xdiff = a[0] - b[0]
                ydiff = a[1] - b[1]
                xsm, xbig = b[0], a[0]
                ysm, ybig = b[1], a[1]
                if a[0] < b[0]:
                    xsm, xbig = a[0], b[0]
                if a[1] < b[1]:
                    ysm, ybig = a[1], b[1]
                currPoints = 2
                for x, y in points:
                    if x >= xsm and x <= xbig and y >= ysm and y <= ybig:
                        if tuple(a) != (x, y) and tuple(b) != (x, y) and xdiff * (b[1] - y) == (b[0] - x) * ydiff:
                            currPoints += 1
                maxPoints = max(maxPoints, currPoints)
        maxPoints = max(maxPoints, 1)
        return maxPoints

# class Solution:
#     def maxPoints(self, points):
#         n = len(points)
#         maxPoints = float('-inf')
#         done = set()
#         for i in range(n):
#             for j in range(i + 1, n):
#                 a = points[i]
#                 b = points[j]
#                 xdiff = a[0] - b[0]
#                 ydiff = a[1] - b[1]
#                 slope = ydiff / xdiff if xdiff != 0 else float('inf') if ydiff > 0 else float('-inf')
#                 yint = a[1] - slope * a[0]
#                 if (slope, yint) in done:
#                     continue
#                 done.add((slope, yint))
#                 currPoints = 0
#                 for x, y in points:
#                     if xdiff * (b[1] - y) == (b[0] - x) * ydiff:
#                         currPoints += 1
#                 maxPoints = max(maxPoints, currPoints)
#         maxPoints = max(maxPoints, 1)
#         return maxPoints