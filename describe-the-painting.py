class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        vals = {}
        for l, r, c in segments:
            vals[l] = vals.get(l, 0) + c
            vals[r] = vals.get(r, 0) - c
        vals = sorted(vals.items())
        res = []
        p = 0
        for i in range(len(vals) - 1):
            p += vals[i][1]
            if p:
                res.append((vals[i][0], vals[i + 1][0], p))
        return res