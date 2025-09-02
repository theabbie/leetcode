from collections import *
from sortedcontainers import SortedList

class SegTree:
    def __init__(self, points):
        self.points = points
        self.tree = defaultdict(SortedList)
        self.build(0, len(points), 1)
        
    def build(self, i, j, k):
        if i + 1 == j:
            self.tree[k].add(self.points[i][1])
            return
        mid = (i + j) // 2
        self.build(i, mid, 2 * k)
        self.build(mid, j, 2 * k + 1)
        self.tree[k] = self.tree[2 * k] + self.tree[2 * k + 1]
        
    def query(self, i, j, xmin, xmax, ymin, ymax, k):
        if self.points[i][0] > xmax or self.points[j - 1][0] < xmin:
            return 0
        if self.points[i][0] >= xmin and self.points[j - 1][0] <= xmax:
            return self.tree[k].bisect_right(ymax) - self.tree[k].bisect_left(ymin)
        mid = (i + j) // 2
        return self.query(i, mid, xmin, xmax, ymin, ymax, 2 * k) + self.query(mid, j, xmin, xmax, ymin, ymax, 2 * k + 1)

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        n = len(xCoord)
        points = [(xCoord[i], yCoord[i], i) for i in range(n)]
        segtree = SegTree(sorted(points))
        up = [-1] * n
        right = [-1] * n
        points.sort(key = lambda p: -p[1])
        last = {}
        for x, y, pos in points:
            if x in last:
                up[pos] = last[x]
            last[x] = pos
        points.sort(key = lambda p: -p[0])
        last = {}
        for x, y, pos in points:
            if y in last:
                right[pos] = last[y]
            last[y] = pos
        res = 0
        for i in range(n):
            if up[i] != -1 and right[i] != -1 and yCoord[up[i]] == yCoord[up[right[i]]]:
                if segtree.query(0, len(points), xCoord[i], xCoord[right[i]], yCoord[i], yCoord[up[i]], 1) == 4:
                    res = max(res, (xCoord[right[i]] - xCoord[i]) * (yCoord[up[i]] - yCoord[i]))
        if res == 0:
            res = -1
        return res