t = int(input())

def printknapSack(W, wt):
    n = len(wt)
    val = wt
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    res = K[n][W]
    w = W
    op = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            op.append(wt[i - 1])
            res = res - val[i - 1]
            w = w - wt[i - 1]
    return (res, op)

for tt in range(1, 1 + t):
    res = "IMPOSSIBLE"
    n, x, y = map(int, input().split())
    total = n * (n + 1) // 2
    if (x * total) % (x + y) == 0:
        curr = x * total // (x + y)
        currval, vals = printknapSack(curr, list(range(1, 1 + n)))
        print(currval, vals)
        if currval == curr:
            res = "POSSIBLE"
    print(f"Case #{tt}: {res}")
    if res == "POSSIBLE":
        print(len(vals))
        print(*vals)
