import math

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    f = lambda x: (a + x) * math.ceil(b / (a + x)) - b + x
    res = float('inf')
    x = 0
    while x * x <= max(a, b):
        res = min(res, f(x))
        x += 1
    print(res)