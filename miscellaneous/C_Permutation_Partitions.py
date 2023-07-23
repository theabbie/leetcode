M = 998244353

n, k = map(int, input().split())

arr = list(map(int, input().split()))


pos = []

for i in range(n):
    if n - k + 1 <= arr[i] <= n:
        pos.append(i)

res = 1

for i in range(len(pos) - 1):
    res *= pos[i + 1] - pos[i]
    res %= M

print(n * (n + 1) // 2 - (n - k) * (n - k + 1) // 2, res)