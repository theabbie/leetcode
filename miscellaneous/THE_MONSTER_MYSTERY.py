t = int(input())

for _ in range(t):
    n = int(input())
    res = n
    i = 2
    while i *i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            res -= res // i
    if n > 1:
        res -= res // n
    print(res)