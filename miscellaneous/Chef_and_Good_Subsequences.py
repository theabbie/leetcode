from collections import Counter

M = 10 ** 9 + 7

n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr = list(Counter(arr).values())

n = len(arr)

k = min(k, n)

dp = [[0] * (k + 1) for _ in range(n)]

for i in range(1, k + 1):
    dp[0][i] = arr[0]

for i in range(1, n):
    for pick in range(1, k + 1):
        dp[i][pick] = arr[i] * (dp[i - 1][pick - 1] + 1) + dp[i - 1][k]
        dp[i][pick] %= M

print((dp[n - 1][k] + 1) % M)