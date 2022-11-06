t = int(input())

def getctr(n):
    res = [0] * n
    i = 0
    j = n - 1
    v = n
    while i <= j:
        if i > 0:
            res[i] = res[i - 1] + v
            res[j] = res[j + 1] + v
        else:
            res[i] = n
            res[j] = n
        i += 1
        j -= 1
        v -= 2
    return res

for _ in range(t):
    s = list(map(int, input()))
    n = len(s)
    ctr = getctr(n)
    p = [0]
    pall = [0]
    for i in range(n):
        p.append(p[-1] + ctr[i] * s[i])
        pall.append(pall[-1] + ctr[i])
    newp = [pall[i] - 2 * p[i] for i in range(n + 1)]
    res = p[-1]
    minyet = float('inf')
    for el in newp:
        minyet = min(minyet, el)
        res = max(res, el - minyet + p[-1])
    print(res)