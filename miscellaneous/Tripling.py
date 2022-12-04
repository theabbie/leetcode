import sys

sys.setrecursionlimit(10**6)

M = 998244353


def numsubs(a, b, c, n):
    dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = 1 + dp[i - 1][j][k] + dp[i][j - 1][k] + dp[i][j][k - 1]
                else:
                    dp[i][j][k] = dp[i - 1][j][k] + dp[i][j - 1][k] + dp[i][j][k - 1] + dp[i - 1][j - 1][k - 1]
    return dp[n][n][n]


n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(numsubs(a, b, c, n) % M)