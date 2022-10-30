t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    incend = [1] * n
    decend = [1] * n
    incstart = [1] * n
    decstart = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            incend[i] = incend[i - 1] + 1
        if arr[i] < arr[i - 1]:
            decend[i] = decend[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            incstart[i] = incstart[i + 1] + 1
        if arr[i] > arr[i + 1]:
            decstart[i] = decstart[i + 1] + 1
    dp = [(0, 0)] * n
    dp[0] = (1, 1)
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            dp[i] = (dp[i - 1][0] + 1, 1)
        elif arr[i] < arr[i - 1]:
            dp[i] = (1, dp[i - 1][1] + 1)
    print(dp)