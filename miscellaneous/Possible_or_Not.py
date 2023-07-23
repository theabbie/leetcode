t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    res = (1 << 32) - 1
    ctr = 0
    for el in arr:
        valid = True
        for b in range(32):
            if m & (1 << b) and not el & (1 << b):
                valid = False
                break
        if valid:
            ctr += 1
            res &= el
    if ctr > 0:
        print("YES" if res == m else "NO")
    else:
        print("NO")