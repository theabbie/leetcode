from collections import defaultdict

t = int(input())

M = 10 ** 9 + 7

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    p = [0] * (n + 1)
    for i in range(n):
        if s[i] in "aeiou":
            p[i + 1] += p[i] + 1
        else:
            p[i + 1] += p[i]
    dp = [0] * (n + 1)
    dp[n] = 1
    prefsum = defaultdict(int)
    for i in range(n, -1, -1):
        dp[i] += prefsum[p[i] + k]
        dp[i] %= M
        prefsum[p[i]] += dp[i]
        prefsum[p[i]] %= M
    print(dp[0])