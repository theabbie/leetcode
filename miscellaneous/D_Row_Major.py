from collections import Counter

N = 1 + 10 ** 6

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

def getfactors(primes, i, n, res, curr):
    if i >= n:
        res.add(curr)
        return
    xx = curr
    for j in range(primes[i][1] + 1):
        getfactors(primes, i + 1, n, res, xx)
        xx *= primes[i][0]

t = int(input())

for _ in range(t):
    n = int(input())
    primes = Counter()
    curr = n
    while curr > 1:
        primes[sp[curr]] += 1
        curr //= sp[curr]
    factors = set()
    getfactors(list(primes.items()), 0, len(primes), factors, 1)
    res = [""] * n
    for i in range(n):
        for c in range(26):
            cc = chr(ord('a') + c)
            valid = True
            for p in factors:
                if i >= p and res[i - p] == cc:
                    valid = False
                    break
            if valid:
                res[i] = cc
                break
    print("".join(res))