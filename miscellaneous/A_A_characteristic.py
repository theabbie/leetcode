t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    res = [1] * n
    numones = n * (n - 1) // 2
    negs = 0
    while numones > k:
        oldones = numones
        numones -= n - negs - 1
        numones += negs
        if numones > oldones:
            break
        negs += 1
    if numones != k:
        print("NO")
        continue
    for i in range(negs):
        if i < n:
            res[i] = -1
    print("YES")
    print(*res)