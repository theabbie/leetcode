from collections import defaultdict

n = int(input())

arr = list(map(int, input().split()))

ctr = defaultdict(int)

for el in arr:
    ctr[el] += 1

print(dict(ctr))

res = 0

for el in ctr:
    if (el - 1) not in ctr and (el + 1) not in ctr:
        res += el * ctr[el]
        del ctr[el]

print(res)