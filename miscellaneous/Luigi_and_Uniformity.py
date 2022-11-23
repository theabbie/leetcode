t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    g = arr[0]
    for el in arr:
        g = gcd(g, el)
    res = 0
    for el in arr:
        if el // g != 1:
            res += 1
    print(res)