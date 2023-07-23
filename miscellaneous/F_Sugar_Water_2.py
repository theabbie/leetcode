m, n, k = map(int, input().split())

a = []
b = []

for _ in range(m):
    x, y = map(int, input().split())
    a.append((x, x + y))

for _ in range(n):
    x, y = map(int, input().split())
    b.append((x, x + y))

print(a, b)