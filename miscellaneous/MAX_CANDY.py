t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (n + 2)
    for i in range(n - 1, -1, -1):
        dp[i] = max(arr[i] + dp[i + 2], dp[i + 1])
        dp[i] = max(dp[i], dp[i + 1])
    print(dp[0])
