t = int(input())

for _ in range(t):
    n = int(input())
    if n & 1:
        gap = n // 2
        res = [n]
        for x in range(n - 1):
            res.append(1 + (n + res[-1] - 1 - gap) % n)
        print(*res)
    else:
        i = n // 2 + 1
        j = 1
        res = []
        for x in range(n):
            if x % 2 == 0:
                res.append(i)
                i += 1
            else:
                res.append(j)
                j += 1
        print(*res)