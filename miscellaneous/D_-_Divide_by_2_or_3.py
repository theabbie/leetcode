n = int(input())

arr = list(map(int, input().split()))

diff = []

for el in arr:
    tw = th = 0
    while el % 2 == 0:
        el = el >> 1
        tw += 1
    while el % 3 == 0:
        el = el // 3
        th += 1
    diff.append((el, tw, th))

pos = True

mintw = float('inf')
minth = float('inf')

for i in range(n):
    if diff[i][0] != diff[0][0]:
        pos = False
        break
    mintw = min(mintw, diff[i][1])
    minth = min(minth, diff[i][2])

res = 0

for i in range(n):
    res += diff[i][1] - mintw
    res += diff[i][2] - minth

if not pos:
    print(-1)
else:
    print(res)