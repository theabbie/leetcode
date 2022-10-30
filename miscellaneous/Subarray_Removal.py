t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    newarr = []
    i = 0
    res = 0
    while i < n:
        ctr = 1
        while i < n - 1 and arr[i] == arr[i + 1]:
            i += 1
            ctr += 1
        if arr[i] == 0:
            newarr.append([0])
        else:
            if ctr > 3:
                res += 1
            newarr.append(1)
        i += 1
    print(newarr)
    print(res)