t = int(input())

def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

for _ in range(t):
    n, m, tx, ty, d = map(int, input().split())
    res = float('inf')
    lr = tx - d <= 1 and tx + d >= n
    tb = ty - d <= 1 and ty + d >= m
    if lr or tb:
        print(-1)
        continue
    for x0, y0, x1, y1 in [(tx - d - 1, ty, tx, ty + d + 1), (tx, ty - d - 1, tx + d + 1, ty)]:
        res = min(res, dist(1, 1, x0, y0) + dist(x0, y0, x1, y1) + dist(x1, y1, n, m))
    print(res)