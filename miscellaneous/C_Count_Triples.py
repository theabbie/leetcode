from collections import Counter
from itertools import permutations

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

actr = Counter(a)
bctr = Counter(b)
cctr = Counter(c)

x = 1

res = 0

while x * x * x <= m:
    if m % x == 0:
        mm = m // x
        y = x
        while y * y <= mm:
            if mm % y == 0:
                for aa, bb, cc in set(permutations([x, y, m // (x * y)])):
                    res += actr[aa] * bctr[bb] * cctr[cc]
            y += 1
    x += 1

print(res)