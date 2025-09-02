class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        res = float('-inf')
        for a in '01234':
            for b in '01234':
                if a == b:
                    continue
                arr = [1 if c == a else (-1 if c == b else 0) for c in s]
                aa = [1 if c == a else 0 for c in s]
                bb = [1 if c == b else 0 for c in s]
                pa = [0] * (n + 1)
                pb = [0] * (n + 1)
                p = [0] * (n + 1)
                for i in range(n):
                    p[i + 1] = p[i] + arr[i]
                    pa[i + 1] = pa[i] + aa[i]
                    pb[i + 1] = pb[i] + bb[i]
                mn = [[float('inf'), float('inf')], [float('inf'), float('inf')]]
                i = 0
                for j in range(n + 1):
                    while j - i >= k and pa[j] - pa[i] > 0 and pb[j] - pb[i] > 0:
                        mn[pa[i] % 2][pb[i] % 2] = min(mn[pa[i] % 2][pb[i] % 2], p[i])
                        i += 1
                    res = max(res, p[j] - mn[1 - (pa[j] % 2)][pb[j] % 2])
        return res