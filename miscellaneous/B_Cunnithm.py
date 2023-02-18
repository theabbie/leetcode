n, m = map(int, input().split())

points = []

for _ in range(n):
    l, r = map(int, input().split())
    points.append((l, 1))
    points.append((r + 1, -1))

points.sort()

