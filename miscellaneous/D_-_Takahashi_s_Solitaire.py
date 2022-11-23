from collections import Counter

n, M = map(int, input().split())

arr = list(map(int, input().split()))

ctr = Counter(arr)

total = sum(arr)

res = total

for el in ctr:
    if el == 0 or (M + el - 1) % M not in ctr:
        curr = 0
        rem = n
        while el in ctr and rem > 0:
            curr += ctr[el] * el
            el = (el + 1) % M
            rem -= ctr[el]
        res = min(res, total - curr)

print(res)