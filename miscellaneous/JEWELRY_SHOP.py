t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    g = d = sv = 0
    p = [[0, 0, 0]]
    for i in range(n):
        if s[i] == 'G':
            g += 1
        if s[i] == 'D':
            d += 1
        if s[i] == 'S':
            sv += 1
        p.append([g, d, sv])
    prevg = prevd = prevs = -1
    res = float('inf')
    for i in range(n):
        if s[i] == 'G':
            j = min(prevd, prevs)
            if j != -1:
                res = min(res, 3 * (p[i + 1][1] - p[j][1]) + 2 * (p[i + 1][0] - p[j][0]) + p[i + 1][2] - p[j][2])
        if s[i] == 'D':
            j = min(prevg, prevs)
            if j != -1:
                res = min(res, 3 * (p[i + 1][1] - p[j][1]) + 2 * (p[i + 1][0] - p[j][0]) + p[i + 1][2] - p[j][2])
        if s[i] == 'S':
            j = min(prevg, prevd)
            if j != -1:
                res = min(res, 3 * (p[i + 1][1] - p[j][1]) + 2 * (p[i + 1][0] - p[j][0]) + p[i + 1][2] - p[j][2])
        if s[i] == 'G':
            prevg = i
        if s[i] == 'D':
            prevd = i
        if s[i] == 'S':
            prevs = i
    if res == float('inf'):
        print(-1)
    else:
        print(res)