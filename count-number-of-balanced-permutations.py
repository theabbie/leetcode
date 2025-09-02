M = 10 ** 9 + 7

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        f = [1] * (n + 1)
        rf = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = i * f[i - 1]
            f[i] %= M
            rf[i] = pow(f[i], M - 2, M)
        ctr = [0] * 10
        s = 0
        for c in num:
            s += int(c)
            ctr[int(c)] += 1
        if s & 1:
            return 0
        cache = [[[-1] * ((s // 2) + 1) for _ in range(n + 1)] for _ in range(10)]
        def dp(d, l, rem):
            if d > 9:
                return int(l == 0 and rem == 0)
            if cache[d][l][rem] != -1:
                return cache[d][l][rem]
            res = 0
            for take in range(ctr[d] + 1):
                if take > l or d * take > rem:
                    continue
                res += rf[take] * rf[ctr[d] - take] * dp(d + 1, l - take, rem - d * take)
                res %= M
            cache[d][l][rem] = res
            return res
        return (f[n // 2] * f[n - (n // 2)] * dp(0, n // 2, s // 2)) % M