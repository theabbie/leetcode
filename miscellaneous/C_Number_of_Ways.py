from collections import defaultdict


n = int(input())

arr = list(map(int, input().split()))

p = [0]

for el in arr:
    p.append(p[-1] + el)

if p[-1] % 3 != 0:
    print(0)
    exit(0)

k = p[-1] // 3

res = 0

ctr = defaultdict(int)

for i in range(1, n + 1):
    if 2 <= i <= n - 1 and p[i] == 2 * k:
        res += ctr[k]
    ctr[p[i]] += 1

print(res)