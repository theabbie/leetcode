t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rsum = sum(r)
    bsum = sum(b)
    dp = [[[0] * (bsum + 1) for _ in range(rsum + 1)] for __ in range(n + 1)]
    for i in range(n, -1, -1):
        for j in range(rsum + 1):
            for k in range(bsum + 1):
                if i == n:
                    dp[i][j][k] = min(j, k)
                else:
                    x = 0
                    y = 0
                    if j + r[i] <= rsum:
                        x = dp[i + 1][j + r[i]][k]
                    if k + b[i] <= bsum:
                        y = dp[i + 1][j][k + b[i]]
                    dp[i][j][k] = max(dp[i][j][k], x, y)
    print(dp[0][0][0])