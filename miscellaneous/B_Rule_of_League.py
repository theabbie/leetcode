from collections import Counter

t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    x, y = max(x, y), min(x, y)
    if x == 0:
        print(-1)
        continue
    res = list(range(2, n + 1))
    for i in range(2, n + 1):
        res[i - 2] = i - (i - 2) % x
    ctr = Counter(res)
    valid = True
    for i in range(1, n + 1):
        if ctr[i] not in {x, y}:
            print(-1)
            valid = False
            break
    if valid:
        print(*res)