m, n = map(int, input().split())

board = []

for _ in range(m):
    board.append(input())

constant = [[0] * (n + 1) for _ in range(m)]
diff = [[0] * (n + 2) for _ in range(m)]

for i in range(m):
    curr = [0] * n
    for j in range(i, m):
        for k in range(n):
            curr[k] += 1 if board[j][k] == "." else 0
        x = 0
        while x < n:
            ctr = 1
            while x < n - 1 and (curr[x] == j - i + 1) == (curr[x + 1] == j - i + 1):
                ctr += 1
                x += 1
            if curr[x] == j - i + 1:
                constant[j - i][0] += ctr + 1
                constant[j - i][ctr] -= ctr + 1
                diff[j - i][0] -= 1
                diff[j - i][ctr + 1] += 1
            x += 1

for i in range(m):
    for j in range(n):
        constant[i][j + 1] += constant[i][j]
    for j in range(n + 1):
        diff[i][j + 1] += diff[i][j]
    for j in range(n + 1):
        diff[i][j + 1] += diff[i][j]
    print(*[constant[i][j] + diff[i][j] for j in range(n)])