t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arrset = set(arr)
    mex = 0
    while mex in arrset:
        mex += 1
    f = n
    l = -1
    for i in range(n):
        if arr[i] == mex + 1:
            if f == n:
                f = i
            l = i
    if f > l:
        pos = False
        seen = set()
        for el in arr:
            if el in seen:
                pos = True
                break
            seen.add(el)
        print("Yes" if pos else "No")
    else:
        arr[f:l+1] = [mex] * (l - f + 1)
        arrset = set(arr)
        newmex = 0
        while newmex in arrset:
            newmex += 1
        print("Yes" if newmex == mex + 1 else "No")