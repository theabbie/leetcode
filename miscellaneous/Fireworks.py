t = int(input())

def sumdigits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

for _ in range(t):
    n = int(input())
    i = 1
    res = 0
    k = len(str(n))
    while i <= 9 * k and i * i <= n:
        if n % i == 0:
            a, b = i, n // i
            if a == sumdigits(b) or b == sumdigits(a):
                res += 1
        i += 1
    print(res)