n, k = map(int, input().split())

ctr = [0] * k

for i in range(n):
    ctr[i % k] += 1

res = 0

for i in range(k):
    res += (n - i - 1) * ctr[i]

print(res)