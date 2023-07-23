from collections import defaultdict

n, k = map(int, input().split())

points = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    points[1] += b
    points[a + 1] -= b

points = sorted(points.items())

curr = 0

res = 1

for d, diff in points:
    curr += diff
    if curr <= k:
        res = d
        break

print(res)