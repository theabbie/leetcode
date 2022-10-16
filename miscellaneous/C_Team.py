n, m = map(int, input().split())

res = []

if m < n - 1:
    res.append("-1")
elif m == n - 1:
    for i in range(m + n):
        res.append(str(i % 2))
else:
    k1d = m % (n + 1)
    k1 = m // (n + 1)
    k2d = m % n
    k2 = m // n
    res = []
    if k1 + (1 if k1d > 0 else 0) <= 2:
        for i in range(n):
            res.append("1" * k1)
            if k1d > 0:
                res.append("1")
                k1d -= 1
            res.append("0")
        res.append("1" * k1)
        if k1d > 0:
            res.append("1")
            k1d -= 1
    elif k2 + (1 if k2d > 0 else 0) <= 2:
        for i in range(n):
            res.append("1" * k1)
            if k1d > 0:
                res.append("1")
                k1d -= 1
            res.append("0")
    else:
        res.append("-1")

print("".join(res))