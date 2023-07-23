t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    res = m // 2
    if res <= m - res:
        res += 1
    print(res)