import math

t = int(input())

for _ in range(t):
    n, k, g = map(int, input().split())
    pay = math.ceil(g / 2) - 1
    x = k * g // pay if pay > 0 else float('inf')
    x = min(x, n - 1)
    res = pay * x
    val = k * g - x * pay
    r = val % g
    if r < math.ceil(g / 2):
        res += r
    else:
        res -= g - r
    print(res)