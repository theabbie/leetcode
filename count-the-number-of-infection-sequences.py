M = 10 ** 9 + 7

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = i * f[i - 1]
            f[i] %= M
        count = lambda m, n: (f[m + n] * pow(f[m], M - 2, M) * pow(f[n], M - 2, M)) % M
        gaps = []
        if sick[0] > 0:
            gaps.append((sick[0], True))
        for i in range(len(sick) - 1):
            if sick[i + 1] - sick[i] > 1:
                gaps.append((sick[i + 1] - sick[i] - 1, False))
        if sick[-1] < n - 1:
            gaps.append((n - sick[-1] - 1, True))
        res = 1
        l = 0
        for g, once in gaps:
            res *= (pow(2, g - 1, M) if not once else 1) * count(l, g)
            res %= M
            l += g
        return res