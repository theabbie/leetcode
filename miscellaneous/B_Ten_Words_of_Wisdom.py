t = int(input())

res = []

for _ in range(t):
    n = int(input())
    cres = (0, -1)
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10:
            cres = max(cres, (b, i + 1))
    res.append(cres[1])

print(*res)