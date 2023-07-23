from collections import Counter

s = input()
t = input()

y = w = 0

ctr = Counter(t)

for c in s:
    if ctr[c] > 0:
        y += 1
        ctr[c] -= 1
    else:
        w += 1

print(y, w)