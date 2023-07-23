t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and arr[i] == arr[i + 1]:
            ctr += 1
            i += 1
        if arr[i] == 0:
            res = max(res, ctr)
        i += 1
    print(res)