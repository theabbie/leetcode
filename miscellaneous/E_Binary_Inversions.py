t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = 0
    val = 0
    inv = [0] * n
    revinv = [0] * n
    for i in range(n - 1, -1, -1):
        inv[i] = ctr
        if arr[i] == 0:
            ctr += 1
        else:
            val += ctr
    ctr = 0
    for i in range(n):
        revinv[i] = ctr
        if arr[i] == 1:
            ctr += 1
    res = val
    for i in range(n):
        if arr[i] == 0:
            res = max(res, val - revinv[i] + inv[i])
        else:
            res = max(res, val - inv[i] + revinv[i])
    print(res)