from collections import Counter

M = 10 ** 9 + 7
N = 10001
f = [1] * (N + 15)
for i in range(1, N + 15):
    f[i] = i * f[i - 1]
    f[i] %= M
    
sp = [1] * N
v = [False] * N

for i in range(2, N, 2):
    sp[i] = 2

for i in range(3, N, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < N:
            v[j * i] = True
            sp[j * i] = i
            j += 2

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        count = lambda n, k: (f[n + k - 1] * pow(f[n] * f[k - 1], M - 2, M)) % M
        res = []
        for n, k in queries:
            ctr = Counter()
            while k > 1:
                ctr[sp[k]] += 1
                k //= sp[k]
            curr = 1
            for el in ctr:
                curr *= count(ctr[el], n)
                curr %= M
            res.append(curr)
        return res