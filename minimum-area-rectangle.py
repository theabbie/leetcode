from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        res = float('inf')
        pmap = defaultdict(set)
        for x, y in points:
            pmap[x].add(y)
        xlist = sorted(pmap.keys())
        m = len(xlist)
        for i in range(m):
            for j in range(i + 1, m):
                l = xlist[j] - xlist[i]
                ypoints = sorted(set.intersection(pmap[xlist[i]], pmap[xlist[j]]))
                p = len(ypoints)
                for k in range(p - 1):
                    res = min(res, l * (ypoints[k + 1] - ypoints[k]))
        if res == float('inf'):
            return 0
        return res