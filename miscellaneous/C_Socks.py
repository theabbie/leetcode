from collections import Counter

n = int(input())

arr = list(map(int, input().split()))

ctr = Counter(arr)

res = 0

for el in ctr:
    res += ctr[el] // 2

print(res)