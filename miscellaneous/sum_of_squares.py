import math

def getPrimes(n):
    c = 2
    res = []
    while n > 1:
        if n % c == 0:
            res.append(c)
            n //= c
        else:
            c += 1
    return res

def getPair(p):
    i = 0
    j = int(math.sqrt(p))
    while i <= j:
        c = i * i + j * j
        if c < p:
            i += 1
        elif c > p:
            j -= 1
        else:
            return (i, j)
    return -1

def sumOfSquares(n):
    res = (0, 1)
    primes = getPrimes(n)
    for p in primes:
        c = getPair(p)
        if c == -1:
            return res
        print(p, c)
        res = tuple(sorted([c[1] * res[1] - c[0] * res[0], res[0] * c[1] + res[1] * c[0]]))
    return res

# 0, 1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20, 25, 26, 29, 32

for i in range(1, 101):
    print(i, getPair(i))

while True:
    n = int(input("Number? "))
    print(sumOfSquares(n))