t = int(input())

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    a, b, c, d = map(int, input().split())
    if (a + 1) % b == (c + 1) % d:
        print(1)
    else:
        print(b * d // GCD(b, d) - a % b)