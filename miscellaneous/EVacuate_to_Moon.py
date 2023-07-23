t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    a = sorted(map(int, input().split()), reverse = True)
    b = sorted(map(int, input().split()), reverse = True)
    for i in range(m):
        b[i] *= h
    res = 0
    for i in range(n):
        if i < m:
            res += min(a[i], b[i])
    print(res)