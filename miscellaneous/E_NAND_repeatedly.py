n = int(input())

s = list(map(int, input()))

dp = [[0, 0] for _ in range(n + 1)]

res = 0

for i in range(n - 1, -1, -1):
    dp[i][0] += dp[i + 1][1]
    dp[i][1] += 1 + dp[i + 1][0]
    res += dp[i][s[i]]

print(res)