t = int(input())

for _ in range(t):
    n = int(input())
    print(n)
    res = list(range(1, n + 1))
    print(*res)
    for i in range(1, n):
        res[i], res[i - 1] = res[i - 1], res[i]
        print(*res)