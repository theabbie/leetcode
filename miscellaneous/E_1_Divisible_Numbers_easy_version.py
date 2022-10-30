t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    a, b, c, d = map(int, input().split())
    m = c - a
    n = d - b
    found = False
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            print(x, y, gcd(a * y + b * x + x * y, a * b))
    print()