t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    if k > m * n:
        print("NO")
        continue
    if k == m * n:
        print("YES")
        continue
    i = 1
    pos = False
    for y in range(min(n, k // m) + 1):
        if (k - y * m) % (n - y) == 0:
            x = (k - y * m) // (n - y)
            if 0 <= x <= m:
                pos = True
                break
    print("YES" if pos else "NO")