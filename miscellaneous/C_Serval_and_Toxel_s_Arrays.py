t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    ops = []
    opgroups = [[] for _ in range(n)]
    for i in range(n):
        opgroups[i].append((0, arr[i]))
    for i in range(m):
        p, v = map(int, input().split())
        ops.append((p - 1, v))
        opgroups[p - 1].append((i + 1, v))
    for i in range(n):
        opgroups[i].append((m + 1, 0))
    res = 2 * n * m * (m + 1) // 2
    ctr = [0] * (n + m + 1)
    for i in range(n):
        l = len(opgroups[i])
        for j in range(l - 1):
            ctr[opgroups[i][j][1]] += opgroups[i][j + 1][0] - opgroups[i][j][0]
    for el in ctr:
        res -= el * (el - 1) // 2
    print(res)