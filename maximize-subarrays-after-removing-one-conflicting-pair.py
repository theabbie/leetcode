class Solution:
    def maxSubarrays(self, n, conflictingPairs):
        m = len(conflictingPairs)
        vp = [[] for _ in range(n)]
        for i, (l, r) in enumerate(conflictingPairs):
            l -= 1; r -= 1
            if l > r: l, r = r, l
            vp[l].append((r, i))
        INF = n
        min1 = [INF] * n
        min2 = [INF] * n
        id1 = [-1] * n
        r1 = INF; r2 = INF; i1 = -1; i2 = -1
        for i in range(n - 1, -1, -1):
            for r, idx in vp[i]:
                if r < r1:
                    r2, i2 = r1, i1
                    r1, i1 = r, idx
                elif r < r2:
                    r2, i2 = r, idx
            min1[i], min2[i], id1[i] = r1, r2, i1
        base = 0
        delta = [0] * m
        for i in range(n):
            r1b = min1[i] if min1[i] < n else n
            r2b = min2[i] if min2[i] < n else n
            base += r1b - i
            k = id1[i]
            if k >= 0:
                delta[k] += (r2b - i) - (r1b - i)
        ans = base
        for d in delta:
            if base + d > ans:
                ans = base + d
        return ans
