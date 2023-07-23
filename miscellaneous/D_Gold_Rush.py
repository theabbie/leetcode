from collections import Counter

t = int(input())

N = 1 + 10 ** 7

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

for _ in range(t):
    n, m = map(int, input().split())
    nprimes = Counter()
    mprimes = Counter()
    all = set()
    curr = n
    while curr > 1:
        nprimes[sp[curr]] += 1
        all.add(sp[curr])
        curr //= sp[curr]
    curr = m
    while curr > 1:
        mprimes[sp[curr]] += 1
        all.add(sp[curr])
        curr //= sp[curr]
    pos = True
    for p in all:
        if p == 2:
            if mprimes[p] < nprimes[p]:
                pos = False
        elif p == 3:
            if nprimes[p] < mprimes[p]:
                pos = False
        else:
            if nprimes[p] != mprimes[p]:
                pos = False
    if pos:
        if mprimes[2] - nprimes[2] > nprimes[3] - mprimes[3]:
            pos = False
    print("YES" if pos else "NO")