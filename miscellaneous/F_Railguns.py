t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    q = map(int, input().split())
    xblocks = [set() for _ in range(m)]
    yblocks = [set() for _ in range(n)]
    for _ in range(t):
        t, d, coord = map(int, input().split())
        if d == 1:
            