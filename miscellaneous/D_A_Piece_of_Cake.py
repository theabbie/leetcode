from collections import Counter
import bisect

w, h = map(int, input().split())

n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

nxcuts = int(input())

xcuts = [0] + list(map(int, input().split())) + [w]

nycuts = int(input())

ycuts = [0] + list(map(int, input().split())) + [h]

ctr = Counter()

minval = float('inf')
maxval = float('-inf')

for x, y in points:
    xx = bisect.bisect_left(xcuts, x)
    yy = bisect.bisect_left(ycuts, y)
    ctr[(xx, yy)] += 1
    maxval = max(maxval, ctr[(xx, yy)])
    
for xx, yy in ctr:
    minval = min(minval, ctr[(xx, yy)])

if len(ctr) < (nxcuts + 1) * (nycuts + 1) or n < (nxcuts + 1) * (nycuts + 1):
    minval = 0

print(minval, maxval)