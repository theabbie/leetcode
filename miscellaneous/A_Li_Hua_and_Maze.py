t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    a, b, c, d = map(int, input().split())
    res = 4
    curr = 0
    for x, y in [(a + 1, b), (a, b + 1), (a - 1, b), (a, b - 1)]:
        if 1 <= x <= m and 1 <= y <= n and (x, y) != (c, d):
            curr += 1
    res = min(res, curr)
    curr = 0
    for x, y in [(c + 1, d), (c, d + 1), (c - 1, d), (c, d - 1)]:
        if 1 <= x <= m and 1 <= y <= n and (x, y) != (a, b):
            curr += 1
    res = min(res, curr)
    print(res)