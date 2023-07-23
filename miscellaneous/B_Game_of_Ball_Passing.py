t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = sum(arr)
    arr.sort()
    p = 0
    for i in range(n):
        if p != 0:
            res = min(res, arr[i] // p)
        p += arr[i]
    print(res)