t = int(input())

res = []

for _ in range(t):
    n, m = map(int, input().split())
    k = n // m
    res.append(m * k * (k + 1) // 2)

print(*res)