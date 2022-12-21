t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = [0] * 32
    for el in arr:
        for b in range(32):
            if el & (1 << b):
                ctr[b] += 1
    maxval = 0
    minval = 0
    for b in range(32):
        if ctr[b] > 0:
            maxval |= 1 << b
        if ctr[b] == n:
            minval |= 1 << b
    print(maxval - minval)