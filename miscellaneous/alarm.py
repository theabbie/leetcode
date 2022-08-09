t = int(input())

for _ in range(t):
    n, H, M = map(int, input().split())
    minTime = (float('inf'), float('inf'))
    for __ in range(n):
        h, m = map(int, input().split())
        if (h, m) < (H, M):
            h += 24
        diff = 60 * (h - H) + m - M
        hh = diff // 60
        mm = diff % 60
        minTime = min(minTime, (hh, mm))
    print(*minTime)