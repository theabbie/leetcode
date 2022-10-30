t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    v = arr[0]
    for el in arr:
        v = gcd(v, el)
    if v == 1:
        print(0)
    else:
        res = None
        for i in range(n, 0, -1):
            if gcd(v, i) == 1:
                res = n - i + 1
                break
        print(min(res, 3))