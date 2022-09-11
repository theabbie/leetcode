t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    rects = []
    for __ in range(n):
        h, w = map(int, input().split())
        rects.append((h, w))
    for __ in range(q):
        hs, ws, hb, wb = map(int, input().split())
        