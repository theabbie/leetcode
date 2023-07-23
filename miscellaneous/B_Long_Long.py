t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    res = 0
    s = 0
    while i < n:
        ctr = 1
        negseen = False
        while i < n - 1 and (arr[i] <= 0) == (arr[i + 1] <= 0):
            s += abs(arr[i])
            if arr[i] < 0:
                negseen = True
            i += 1
            ctr += 1
        if arr[i] < 0:
            negseen = True
        s += abs(arr[i])
        if arr[i] <= 0 and negseen:
            res += 1
        i += 1
    print(s, res)