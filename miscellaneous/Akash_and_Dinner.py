t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    v = [(b[i], a[i]) for i in range(n)]
    v.sort()
    i = 0
    res = 0
    d = set()
    for i in range(n):
        if len(d) < k and v[i][1] not in d:
            d.add(v[i][1])
            res += v[i][0]
    if len(d) == k:
        print(res)
    else:
        print(-1)