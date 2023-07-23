t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    valid = [0] * n
    for i in range(n - 1):
        if b[i] <= b[i + 1]:
            valid[i] = 1
    valid[n - 1] = 1
    l = 0
    while l < n and a[l] == b[l]:
        l += 1
    r = n - 1
    while r >= 0 and a[r] == b[r]:
        r -= 1
    res = (0, 0, 0)
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and valid[i] == valid[i + 1]:
            ctr += 1
            i += 1
        if valid[i] == 1:
            if i - ctr + 1 <= l and i + 1 >= r:
                res = max(res, (ctr, i - ctr + 1, min(i + 1, n - 1)))
        i += 1
    print(res[1] + 1, res[2] + 1)