import math

n = int(input())

def factorize(n):
    count = 0
    res = 0
    while n % 2 == 0:
        n >>= 1
        count += 1
    if count > 0:
        res = max(res, 2 * count)
    for i in range(3, int(math.sqrt(n)) + 1):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            res = max(res, i * count)
        i += 2
    if n > 2:
        res = max(res, n)
    return res

def val(x): 
    i = 1
    fact = 1
    for i in range(1, x + 1): 
        fact = fact * i 
        if fact % x == 0: 
            break
    return i

for i in range(1, 101):
    print(i, val(i), factorize(i))