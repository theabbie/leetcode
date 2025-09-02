M = 10 ** 9 + 7

U = 100000
f = [1] * (U + 1)
for i in range(1, U + 1):
    f[i] = i * f[i - 1]
    f[i] %= M
fi = [1] * (U + 1)
fi[U] = pow(f[U], M - 2, M)
for i in range(U - 1, -1, -1):
    fi[i] = (i + 1) * fi[i + 1]
    fi[i] %= M
def comb(a, b):
    if a < b:
        return 0
    return (f[a] * fi[b] * fi[a - b]) % M

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        k = n - k
        mul = (m * pow(m - 1, k - 1, M)) % M
        return (mul * comb(n - 1, k - 1)) % M