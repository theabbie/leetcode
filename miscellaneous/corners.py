t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, list(input()))))
    dp = [[0] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = matrix[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    print("==", dp[-1][-1])