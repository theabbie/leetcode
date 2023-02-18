t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    p = [0]
    z = o = 0
    for el in arr:
        if el == 0:
            z += 1
        else:
            o += 1
        p.append(o - z)
    res = []
    vals = {0: 1}
    pos = {0: 0}
    prev = {}
    for i in range(n + 1):
        if p[i] - 1 in vals:
            vals[p[i]] = 1 + vals[p[i] - 1]
            prev[i] = pos[p[i] - 1]
        else:
            vals[p[i]] = 1
        pos[p[i]] = i
    l = max(vals.values())
    print(l)
    for i in range(n, -1, -1):
        if vals[p[i]] == l:
            curr = i
            res.append(curr + 1)
            while curr in prev:
                curr = prev[curr]
                res.append(curr + 1)
            res.reverse()
            break
    print(*res)