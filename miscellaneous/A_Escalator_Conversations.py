t = int(input())

for _ in range(t):
    n, m, k, H = map(int, input().split())
    heights = map(int, input().split())
    res = 0
    for h in heights:
        if h != H and abs(h - H) % k == 0 and abs(h - H) // k <= m - 1:
            res += 1
    print(res)