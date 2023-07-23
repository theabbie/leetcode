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
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter()
    for el in arr:
        curr = el
        while curr > 1:
            ctr[sp[curr]] += 1
            curr //= sp[curr]
    res = 0
    rem = 0
    for p in ctr:
        res += ctr[p] // 2
        rem += ctr[p] % 2
    res += rem // 3
    print(res)