n, a = map(int, input().split())

w = []
x = []
v = []

for _ in range(n):
    cw, cx, cv = map(int, input().split())
    w.append(cw)
    x.append(cx)
    v.append(cv)

def getVal(t, x, v, w, n, a):
    vals = sorted([(x[i] + t * v[i], w[i]) for i in range(n)])
    i = 0
    res = 0
    for j in range(n):
        while vals[j][0] - vals[i][0] > a:
            i += 1
        if vals[j][0] - vals[i][0] <= a:
            curr = 0
            for x in range(i, j + 1):
                curr += vals[x][1]
            res = max(res, curr)
    return res

beg = 0
end = 10000
res = 0

while beg < end:
    mid = (beg + end) // 2
    mid1val = getVal(mid, x, v, w, n, a)
    mid2val = getVal(mid + 1, x, v, w, n, a)
    if mid1val >= mid2val:
        res = max(res, mid1val)
        end = mid - 1
    else:
        res = max(res, mid2val)
        beg = mid + 1

print(res)