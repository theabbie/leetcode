import math

t  = int(input())

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

for _ in range(t):
    n = int(input())
    k = 0
    while n % 4 == 0:
        k += 1
        n = n >> 2
    res = getPair(n)
    if res == -1:
        print(-1)
    else:
        print(res[0] * (1 << k), res[1] * (1 << k))