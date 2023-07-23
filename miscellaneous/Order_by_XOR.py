t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    res = 0
    abq = False
    bcq = False
    for i in range(29, -1, -1):
        ab = 1 if a & (1 << i) else 0
        bb = 1 if b & (1 << i) else 0
        cb = 1 if c & (1 << i) else 0
        if not abq and ab > bb:
            res |= (1 << i)
        if not bcq and bb > cb:
            res |= (1 << i)
        if ab != bb:
            abq = True
        if bb != cb:
            bcq = True
    if (a ^ res) < (b ^ res) < (c ^ res):
        print(res)
    else:
        print(-1)