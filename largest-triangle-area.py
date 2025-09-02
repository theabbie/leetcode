import numpy as np
from scipy.spatial import ConvexHull

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        pts = np.array(points)
        if len(pts) < 3:
            return 0.0
        hull = ConvexHull(pts)
        hull_points = pts[hull.vertices]
        h = len(hull_points)
        if h < 3:
            return 0.0
        ext = np.concatenate([hull_points, hull_points])
        def tri_area(a, b, c):
            return abs(np.cross(b - a, c - a)) / 2.0
        max_area = 0.0
        for i in range(h):
            k = i + 2
            for j in range(i + 1, i + h):
                while k + 1 < i + h and tri_area(ext[i], ext[j], ext[k + 1]) > tri_area(ext[i], ext[j], ext[k]):
                    k += 1
                max_area = max(max_area, tri_area(ext[i], ext[j], ext[k]))
        return max_area