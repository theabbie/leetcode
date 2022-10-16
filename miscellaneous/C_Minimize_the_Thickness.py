t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    p = [0]
    exists = {}
    for el in arr:
        p.append(p[-1] + el)
        exists[p[-1]] = len(p) - 1
    res = n
    for i in range(1, n + 1):
        if p[-1] % p[i] == 0:
            curr = i
            k = 1
            while p[i] * k < p[-1] and (p[i] * (k + 1)) in exists:
                curr = max(curr, exists[p[i] * (k + 1)] - exists[p[i] * k])
                k += 1
            if p[i] * k == p[-1]:
                res = min(res, curr)
    print(res)