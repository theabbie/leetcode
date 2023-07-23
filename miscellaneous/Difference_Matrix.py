t = int(input())

for _ in range(t):
    n = int(input())
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            k = n * i + j
            if k * 2 < n * n:
                mat[i][j] = 2 * k + 1
            else:
                mat[i][j] = k * 2 - n * n + 1
                if n % 2 == 0:
                    mat[i][j] += 1
    print("\n".join(" ".join(map(str, r)) for r in mat))