t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    cc = list(map(int, input().split()))
    p = 0
    for el in aa:
        valid = True
        for b in range(32):
            if el & (1 << b) and not x & (1 << b):
                valid = False
                break
        if valid:
            p |= el
        else:
            break
    for el in bb:
        valid = True
        for b in range(32):
            if el & (1 << b) and not x & (1 << b):
                valid = False
                break
        if valid:
            p |= el
        else:
            break
    for el in cc:
        valid = True
        for b in range(32):
            if el & (1 << b) and not x & (1 << b):
                valid = False
                break
        if valid:
            p |= el
        else:
            break
    print("Yes" if p == x else "No")