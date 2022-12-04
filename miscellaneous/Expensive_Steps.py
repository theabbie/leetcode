t = int(input())

for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    res = abs(c - a) + abs(d - b)
    x = [min(a, n - a + 1), min(b, n - b + 1)]
    y = [min(c, n - c + 1), min(d, n - d + 1)]
    res = min(res, min(x) + min(y))
    print(res)