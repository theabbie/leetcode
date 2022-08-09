from collections import defaultdict

n = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

pos = defaultdict(int)

next = {}

for i in range(n - 1, -1, -1):
    j = pos[arr[i] + 1]
    dp[i] = dp[j] + 1
    next[i] = j
    if dp[i] > dp[pos[arr[i]]]:
        pos[arr[i]] = i

k = max(range(n), key = lambda i: dp[i])

res = []

while k in next:
    res.append(k + 1)
    k = next[k]

res.append(k + 1)

print(len(res))
print(*res)