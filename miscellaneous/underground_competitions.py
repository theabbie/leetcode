t = int(input())

for _ in range(t):
    n, k, r, c = map(int, input().split())
    res = [["."] * k for _ in range(k)]
    r = (r - 1) % k
    c = (c - 1) % k
    res[r][c] = "X"
    for i in range(1, k + 1):
        res[(r + i) % k][(c + i) % k] = "X"
    for i in range(n):
        for j in range(n):
            print(res[i % k][j % k], end = "")
        print()