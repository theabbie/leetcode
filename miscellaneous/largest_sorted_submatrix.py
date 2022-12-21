def largest(matrix):
    m, n = len(matrix), len(matrix[0])
    good = lambda i, j: 1 if (i == 0 or matrix[i][j] >= matrix[i - 1][j]) and (j == 0 or matrix[i][j] >= matrix[i][j - 1]) else 0
    p = [[0] * (n + 1) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            p[i][j + 1] += good(i, j) + p[i][j]
    print([[good(i, j) for j in range(n)] for i in range(m)])
    res = 0
    for i in range(n):
        for j in range(i, n):
            k = 0
            while k < m:
                ctr = 1
                while k < m - 1 and p[k][j + 1] - p[k][i] == p[k + 1][j + 1] - p[k + 1][i]:
                    k += 1
                    ctr += 1
                if p[k][j + 1] - p[k][i] == j - i + 1:
                    res = max(res, ctr * (j - i + 1))
                k += 1
    return res

matrix = [[1, 4, 5],
          [2, 3, 3],
          [3, 4, 1]]

print(largest(matrix))