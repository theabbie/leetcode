import math

a, b = map(int, input().split())

def val(x, a, b):
    return b * x + a * math.sqrt(1 + x) / (1 + x)

x = (a / (2 * b)) ** (2/ 3) - 1

if x < 0:
    print(val(0, a, b))
else:
    print(min(val(int(x), a, b), val(int(x) + 1, a, b)))