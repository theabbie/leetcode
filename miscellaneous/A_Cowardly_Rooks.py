t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    ctrx = [0] * n
    ctry = [0] * n
    for __ in range(m):
        x, y = map(int, input().split())
        ctrx[x - 1] += 1
        ctry[y - 1] += 1
    if 0 in ctrx or 0 in ctry:
        print("YES")
    else:
        print("NO")