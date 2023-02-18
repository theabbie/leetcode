from collections import Counter

M = 998244353

n = int(input())

arr = list(map(int, input().split()))

res = 1

for i in range(0, n, 3):
    a, b, c = sorted(arr[i:i+3])
    curr = Counter()
    curr[a] += 1
    curr[b] += 1
    curr[c] += 1
    res *= curr[b] * curr[c]
    res %= M

print((res * pow(2, M - 2, M)) % M)