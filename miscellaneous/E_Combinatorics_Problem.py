M = 998244353

from collections import Counter

N = 1 + 10 ** 6
v = [False] * N
spf = [1] * N

for i in range(2, N, 2):
    spf[i] = 2

for i in range(3, N, 2):
    if not v[i]:
        spf[i] = i
        j = i
        while j * i < N:
            if not v[j * i]:
                v[j * i] = True
                spf[j * i] = i
            j += 2


def facts(n, mod):
    res = [1] * (n + 1)
    ctr = Counter()
    for i in range(1, n + 1):
        a = n - i + 1
        b = i
        while a > 1:
            ctr[spf[a]] += 1
            a //= spf[a]
        while b > 1:
            ctr[spf[b]] -= 1
            b //= spf[b]
        for p in ctr:
            res[i] *= pow(p, ctr[p], mod)
            res[i] %= mod
    return res


print(*facts(1000, 18))
