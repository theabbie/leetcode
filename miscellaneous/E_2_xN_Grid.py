l, m, n = map(int, input().split())

a = []
b = []

for _ in range(m):
    x, y = map(int, input().split())
    a.append([x, y])

for j in range(n):
    x, y = map(int, input().split())
    b.append([x, y])

res = 0

while len(a) > 0 and len(b) > 0:
    ax, ay = a.pop()
    bx, by = b.pop()
    if ay <= by:
        if ax == bx:
            res += ay
        if ay < by:
            b.append((bx, by - ay))
    else:
        if ax == bx:
            res += by
        a.append((ax, ay - by))

print(res)