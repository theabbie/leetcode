t = int(input())

pows = [1] * 32
for b in range(1, 32):
    pows[b] = pows[b - 1] * 2

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    ctr = [0] * 32
    for el in arr:
        for b in range(32):
            if el & 1:
                ctr[b] += 1
            el //= 2
    res = 0
    for b in range(32):
        if ctr[b] != 0 and ctr[b] != n:
            if x & pows[b]:
                if b > 0:
                    res = max(res, (x & ~pows[b]) | (pows[b - 1] - 1))
                else:
                    res = max(res, x & ~pows[0])
            else:
                res = max(res, x)
    print(res)