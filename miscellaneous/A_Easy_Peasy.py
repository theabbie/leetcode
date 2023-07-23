t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    g = 0
    for el in arr:
        g = gcd(g, el)
    i = 0
    while i == 1 or gcd(i, g) != 1:
        i += 1
    print(i)