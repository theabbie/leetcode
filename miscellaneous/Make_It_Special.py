t = int(input())

def count(num, i, n, tight, maxnum, mxx, mnx, cache):
    if i >= n:
        return 1
    maxd = 1
    if tight:
        maxd = int(num[i])
    res = 0
    for d in range(maxd + 1):
        currmxx, currmnx = mxx, mnx
        for b in range
        res += count(num, i + 1, n, tight and d == maxd, maxnum, currmxx, currmnx, cache)
    return res

for _ in range(t):
    n, q = map(int, input().split())
    for _ in range(q):
        l, r = map(int, input().split())
        for x in range(l, r + 1):
            print(sorted([x ^ p for p in range(1, n + 1)]))
        print()