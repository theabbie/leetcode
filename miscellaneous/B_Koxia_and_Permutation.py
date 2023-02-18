t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    res = []
    front = False
    for i in range(n):
        if front:
            res.append(i // 2 + 1)
        else:
            res.append(n - i // 2)
        front = not front
    print(*res)