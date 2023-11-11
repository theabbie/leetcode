t = int(input())

for _ in range(t):
    x, y, n = map(int, input().split())
    res = [y]
    diff = 1
    for _ in range(n - 2):
        res.append(res[-1] - diff)
        diff += 1
    if res[-1] - diff < x:
        print(-1)
        continue
    res.append(x)
    res.reverse()
    print(*res)