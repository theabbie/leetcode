t = int(input())

for _ in range(t):
    n = int(input())
    res = list(range(n, 0, -1))
    i = 0
    while i < n:
        if res[i] == i + 1:
            break
        i += 1
    res[i:] = res[i:][::-1]
    valid = True
    for i in range(n):
        if res[i] == i + 1:
            valid = False
            break
        if not (i > 0 and abs(res[i] - res[i - 1]) == 1) and not (i < n - 1 and abs(res[i] - res[i + 1]) == 1):
            valid = False
            break
    if not valid:
        print(-1)
    else:
        print(*res)