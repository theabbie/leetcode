class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        x = [el[0] for el in points]
        minx = min(x)
        maxx = max(x)
        mid = minx + maxx
        s = set(tuple(p) for p in points)
        for p in s:
            target = mid - p[0]
            if (target, p[1]) not in s:
                return False
        return True