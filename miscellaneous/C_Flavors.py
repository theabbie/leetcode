n = int(input())

flavours = [[] for _ in range(n)]

for _ in range(n):
    f, s = map(int, input().split())
    flavours[f - 1].append(s)

res = 0

mdel = float('-inf')

for i in range(n):
    currmdel = float('-inf')
    a, b = float('-inf'), float('-inf')
    for s in flavours[i]:
        res = max(res, s + mdel)
        currmdel = max(currmdel, s)
        temp, a, b = sorted([a, b, s])
    res = max(res, b + a // 2)
    mdel = max(mdel, currmdel)

print(res)