t = int(input())

pw = [1] * 32

for i in range(1, 32):
    pw[i] = pw[i - 1] * 2

for _ in range(t):
    m, n = map(int, input().split())
    rowsums = [[0] * 32 for _ in range(m)]
    colsums = [[0] * 32 for _ in range(n)]
    mat = []
    for _ in range(m):
        mat.append(list(map(int, input().split())))
    all = [0] * 32
    for i in range(m):
        for j in range(n):
            for b in range(32):
                if mat[i][j] & pw[b]:
                    rowsums[i][b] += 1
                    colsums[j][b] += 1
                    all[b] += 1
    res = 0
    for i in range(m):
        for j in range(n):
            curr = all[:]
            for b in range(32):
                curr[b] -= rowsums[i][b] + colsums[j][b]
                if mat[i][j] & pw[b]:
                    curr[b] += 1
            currval = 0
            for b in range(32):
                if mat[i][j] & pw[b]:
                    currval += pw[b] * (m * n - m - n + 1 - curr[b])
                else:
                    currval += pw[b] * curr[b]
            res = max(res, currval)
    print(res)