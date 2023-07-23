t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(-1)
    else:
        res = []
        while n > 1:
            if ((n + 1) // 2) & 1:
                res.append(1)
                n = (n + 1) // 2
            else:
                res.append(2)
                n = (n - 1) // 2
        res.reverse()
        if len(res) > 40:
            print(-1)
        else:
            print(len(res))
            print(*res)