from functools import cmp_to_key

t = int(input())

def cmp(a, b):
    a1, b1 = a
    a2, b2 = b
    if a1 * b2 < a2 * b1:
        return 1
    return -1

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = [(a[i], b[i]) for i in range(n)]
    x.sort(key = cmp_to_key(cmp))
    res = 0
    p = 0
    for a, b in x:
        res += p * b
        p += a
    print(res)