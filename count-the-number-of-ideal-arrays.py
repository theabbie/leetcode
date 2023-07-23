from collections import defaultdict, Counter

class Solution:
    def idealArrays(self, n, maxValue):
        M = 10 ** 9 + 7
        f = [1] * (n + 1)
        fi = [1] * (n + 1)
        for i in range(2, n + 1):
            f[i] = i * f[i - 1]
            fi[i] = pow(i, M - 2, M) * fi[i - 1]
            f[i] %= M
            fi[i] %= M
        vals = defaultdict(Counter)
        for i in range(1, maxValue + 1):
            vals[1][i] += 1
        ctr = 2
        while ctr <= n:
            done = True
            for prev in vals[ctr - 1]:
                mul = 2
                while prev * mul <= maxValue:
                    vals[ctr][prev * mul] += vals[ctr - 1][prev]
                    mul += 1
                    done = False
            if done:
                break
            ctr += 1
        res = 0
        for i in range(1, ctr + 1):
            l = sum(vals[i].values())
            res += l * f[n - 1] * fi[i - 1] * fi[n - i]
            res %= M
        return res