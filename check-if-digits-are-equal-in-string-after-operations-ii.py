class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def binom_mod2(n, r):
            return 1 if (n & r) == r else 0
        binom5 = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(i + 1):
                if j == 0 or j == i:
                    binom5[i][j] = 1
                else:
                    binom5[i][j] = (binom5[i - 1][j - 1] + binom5[i - 1][j]) % 5
        def lucas(n, r):
            res = 1
            while n or r:
                n_i, r_i = n % 5, r % 5
                if r_i > n_i:
                    return 0
                res = (res * binom5[n_i][r_i]) % 5
                n //= 5
                r //= 5
            return res
        def combine(x2, x5):
            for cand in range(x5, 10, 5):
                if cand % 2 == x2:
                    return cand
            return 0
        def binom_mod10(n, r):
            return combine(binom_mod2(n, r), lucas(n, r))
        n = len(s)
        if n < 2:
            return True
        mod1 = 0
        mod2 = 0
        for i in range(n - 1):
            c = binom_mod10(n - 2, i)
            mod1 = (mod1 + int(s[i]) * c) % 10
            mod2 = (mod2 + int(s[i + 1]) * c) % 10
        return mod1 == mod2