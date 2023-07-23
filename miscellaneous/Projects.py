n = int(input())

mp = {}

projects = []

for _ in range(n):
    a, b, p = map(int, input().split())
    mp[a] = mp[b + 1] = 0
    projects.append((a, b + 1, p))

lefts = [[] for _ in range(len(mp) + 1)]

for i, el in enumerate(sorted(mp)):
    mp[el] = i

for a, b, p in projects:
    lefts[mp[b]].append((mp[a], p))

dp = [0] * (len(mp) + 1)

for i in range(len(mp) + 1):
    if i > 0:
        dp[i] = dp[i - 1]
    for l, p in lefts[i]:
        dp[i] = max(dp[i], p + dp[l])

print(max(dp))