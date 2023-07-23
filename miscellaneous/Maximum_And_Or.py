t = int(input())

pows = [1] * 32
for b in range(1, 32):
    pows[b] = pows[b - 1] * 2

for _ in range(t):
    a, b, c = map(int, input().split())
    res = 1
    for x in range(c, -1, -1):
        i = 1 if a & pows[x] else 0
        j = 1 if b & pows[x] else 0
        mx = max((j | 0) - (i & 0), (j | 1) - (i & 1))
        curr = 0
        if mx == (j | 0) - (i & 0):
            curr += 1
        if mx == (j | 1) - (i & 1):
            curr += 1
        res *= curr
    print(res)