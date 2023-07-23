t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(n):
        res = gcd(res, arr[i] - i - 1)
    print(abs(res))