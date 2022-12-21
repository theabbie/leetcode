from collections import Counter

t = int(input())

def minops(a, b, c):
    if min(a, b, c) < 0:
        return float('inf')
    if b == 0 and c == 0:
        return 0
    if b > 0 and c > 0:
        x = min(b, c)
        return x + minops(a + x, b - x, c - x)
    ar = 1 + minops(a - 1, b + 1, c)
    br = 1 + minops(a - 1, b, c + 1)
    cr = 1 + minops(a, b - 2, c + 2)
    dr = 1 + minops(a, b + 2, c - 2)
    return min(ar, br, cr, dr)

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter()
    for el in arr:
        ctr[el % 3] += 1
    print(minops(ctr[0], ctr[1], ctr[2]))