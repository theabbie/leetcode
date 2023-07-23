n = int(input())

foods = []

for _ in range(n):
    x, taste = map(int, input().split())
    foods.append((x, taste))

dp = [[0, 0] for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    for prevpois in range(2):
        dp[i][prevpois] = dp[i + 1][prevpois]
        if foods[i][0] == 1:
            if not prevpois:
                dp[i][prevpois] = max(dp[i][prevpois], foods[i][1] + dp[i + 1][1])
        else:
            dp[i][prevpois] = max(dp[i][prevpois], foods[i][1] + dp[i + 1][0])

print(dp[0][0])