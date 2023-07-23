from collections import defaultdict

m, n = map(int, input().split())

ur = [[0] * (n + 1) for _ in range(m)]
uc = [[0] * (m + 1) for _ in range(n)]

board = []

for _ in range(m):
    board.append(input())

graph = defaultdict(set)

lastrow = [0] * n

lastcol = [0] * m

for i in range(m):
    for j in range(n):
        if board[i][j] == "#":
            lastrow[j] = i
            lastcol[i] = j
        else:
            graph[(i, j)].add((i, lastcol[i] + 1))
            graph[(i, j)].add((lastrow[j] + 1, j))

lastrow = [m - 1] * n

lastcol = [n - 1] * m

for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if board[i][j] == "#":
            lastrow[j] = i
            lastcol[i] = j
        else:
            graph[(i, j)].add((i, lastcol[i] - 1))
            graph[(i, j)].add((lastrow[j] - 1, j))

stack = [(1, 1)]

v = {(1, 1)}

while len(stack) > 0:
    i, j = stack.pop()
    for x, y in graph[(i, j)]:
        a, b = min((i, j), (x, y))
        c, d = max((i, j), (x, y))
        if a == c:
            ur[a][b] += 1
            ur[a][d + 1] -= 1
        if b == d:
            uc[b][a] += 1
            uc[b][c + 1] -= 1
        if (x, y) not in v:
            v.add((x, y))
            stack.append((x, y))

for i in range(m):
    for j in range(n):
        ur[i][j + 1] += ur[i][j]

for i in range(n):
    for j in range(m):
        uc[i][j + 1] += uc[i][j]

res = 0

for i in range(m):
    for j in range(n):
        if board[i][j] == "." and (ur[i][j] != 0 or uc[j][i] != 0):
            res += 1

print(res)