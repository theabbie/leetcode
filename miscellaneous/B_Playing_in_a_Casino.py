t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cards = [[] for _ in range(m)]
    for _ in range(n):
        curr = list(map(int, input().split()))
        for i in range(m):
            cards[i].append(curr[i])
    for i in range(m):
        cards[i].sort()
    res = 0
    for i in range(m):
        p = 0
        for j in range(n):
            res += j * cards[i][j] - p
            p += cards[i][j]
    print(res)