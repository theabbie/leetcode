class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        p = [0] * (n + 1)
        for i, h in enumerate(hours):
            p[i + 1] = p[i] + 2 * int(h > 8) - 1
        vals = [(p[i], i) for i in range(n + 1)]
        vals.sort()
        minval = float('inf')
        res = 0
        j = 0
        for v, i in vals:
            while j < len(vals) and vals[j][0] < v:
                minval = min(minval, vals[j][1])
                j += 1
            res = max(res, i - minval)
        return res