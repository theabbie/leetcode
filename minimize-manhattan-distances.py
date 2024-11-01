def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def max_manhattan_distance(points):
    candidates = set()
    for a in [-1, 1]:
        for b in [-1, 1]:
            for c in [0, 1]:
                curr = (float('inf') if c == 0 else float('-inf'), -1)
                for i in range(len(points)):
                    val = a * points[i][0] + b * points[i][1]
                    if c == 0:
                        curr = min(curr, (val, i))
                    else:
                        curr = max(curr, (val, i))
                candidates.add(curr[1])
    d = float('-inf')
    res = None
    for i in range(len(points)):
        for j in candidates:
            if manhattan_distance(points[i], points[j]) > d:
                d = manhattan_distance(points[i], points[j])
                res = (points[i], points[j])
    return res

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        a, b = max_manhattan_distance(points)
        res = manhattan_distance(a, b)
        points.remove(a)
        x, y = max_manhattan_distance(points)
        res = min(res, manhattan_distance(x, y))
        points.append(a)
        points.remove(b)
        x, y = max_manhattan_distance(points)
        res = min(res, manhattan_distance(x, y))
        points.append(a)
        return res