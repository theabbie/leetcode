t = int(input())

for _ in range(t):
    n = int(input())
    sides = []
    mside = 0
    for __ in range(n):
        l, h = map(int, input().split())
        sides.append((l, h))
        mside = max(mside, l, h)
    w = 0
    for i in range(n):
        w += min(sides[i])
    print(mside * 2 + w * 2)