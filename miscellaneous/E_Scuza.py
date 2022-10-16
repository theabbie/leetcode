import bisect

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    h = list(map(int, input().split()))
    q = list(map(int, input().split()))
    pf = [0]
    for el in h:
        pf.append(pf[-1] + el)
    newh = []
    pos = {}
    maxval = float('-inf')
    for i, el in enumerate(h):
        maxval = max(maxval, el)
        if el == maxval:
            newh.append(el)
            pos[len(newh) - 1] = i
    res = []
    for k in q:
        j = bisect.bisect_right(newh, k)
        if j == len(newh):
            res.append(pf[-1])
        elif j == 0:
            res.append(0)
        else:
            res.append(pf[pos[j]])
    print(*res)