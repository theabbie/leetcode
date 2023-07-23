def sumd(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())

for _ in range(t):
    n = int(input())
    while gcd(n, sumd(n)) == 1:
        n += 1
    print(n)