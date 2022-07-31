n, x = map(int, input().split())

ranges = []

for i in range(n):
    l, r = map(int, input().split())
    ranges.append([l, r])

points = []

for l, r in ranges:
    points.append((l, r - l + 1))

points.sort()

k = len(points)

curr = 1

res = 0

i = 0

while i < k:
    if points[i][0] >= curr:
        res += (points[i][0] - curr) % x + points[i][1]
        curr = points[i][0] + points[i][1]
    i += 1

print(res)