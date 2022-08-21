t = int(input())

for _ in range(t):
    n = int(input())
    minx, maxx = float('inf'), float('-inf')
    miny, maxy = float('inf'), float('-inf')
    for _ in range(n):
        x, y = map(int, input().split())
        minx = min(minx, x, 0)
        maxx = max(maxx, x, 0)
        miny = min(miny, y, 0)
        maxy = max(maxy, y, 0)
    minx = abs(minx)
    miny = abs(miny)
    print(2 * (minx + maxx + miny + maxy))