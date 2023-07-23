from collections import Counter

s = input()

n = len(s)

res = 0

ctr = Counter()

dctr = [0] * 10

ctr[tuple(dctr)] += 1

for c in s:
    dctr[int(c)] += 1
    dctr[int(c)] %= 2
    x = tuple(dctr)
    res += ctr[x]
    ctr[x] += 1

print(res)