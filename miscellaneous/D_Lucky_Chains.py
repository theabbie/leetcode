import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


cache = {}
 
def smallestprimedivisor(n):
    if n == 1:
        return float('inf')
    if n in cache:
        return cache[n]
    i = 2
    while i * i <= n:
        if n % i == 0:
            res = min(smallestprimedivisor(i), smallestprimedivisor(n // i))
            cache[n] = res
            return res
        i += 1
    cache[n] = n
    return n

t = int(input())

reses = []

for _ in range(t):
    a, b = map(int, input().split())
    n = abs(a - b)
    if n == 1:
        reses.append("-1")
        continue
    if gcd(a, b) != 1:
        reses.append("0")
        continue
    res = float('inf')
    p = smallestprimedivisor(n)
    x, y = p * math.ceil(a / p), p * math.ceil(b / p)
    res = min(res, x - a, y - b)
    reses.append(str(res))

print("\n".join(reses))