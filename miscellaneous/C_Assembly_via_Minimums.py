t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = []
    ctr = n - 1
    i = 0
    while ctr > 0:
        res.append(arr[i])
        i += ctr
        ctr -= 1
    res.append(arr[-1])
    print(*res)