from collections import Counter

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

ctr = Counter()

for el in arr:
    ctr[el % m] += 1

res = 1

for a in ctr:
    for b in ctr:
        if a != b:
            res *= pow(m + a - b, ctr[a] * ctr[b], m)
            res %= m

print(res)