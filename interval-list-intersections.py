class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        points = []
        for a, b in firstList + secondList:
            points.append((a, 1))
            points.append((b + 1, -1))
        points.sort()
        res = []
        p = 0
        for x, d in points:
            p += d
            if p == 2:
                res.append([x, x])
            elif p == 1 and d == -1 and len(res) > 0:
                res[-1][1] = x - 1
        return res