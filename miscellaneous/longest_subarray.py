t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    X = 0
    for el in arr:
        X |= el
    dp = [0] * n
    for i in range(n):
        if arr[i] == X:
            dp[i] = dp[i - 1] + 1 if i > 0 else 1
        else:
            dp[i] = dp[i - 1]
    print(max(dp))