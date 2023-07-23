def valid(board, i, j, l, m, n):
    for x, y in [(i - l, j - l), (i - l, j + l), (i + l, j + l), (i + l, j - l)]:
        if not (0 <= x < m and 0 <= y < n) or board[x][y] != "#":
            return False
    return True

def corner(board, i, j, l, m, n):
    for x, y in [(i - l - 1, j - l - 1), (i - l - 1, j + l + 1), (i + l + 1, j + l + 1), (i + l + 1, j - l - 1)]:
        if 0 <= x < m and 0 <= y < n and board[x][y] == ".":
            return True
    return False

m, n = map(int, input().split())

board = []

for _ in range(m):
    board.append(input())

k = min(m, n)

res = [0] * k

for i in range(m):
    for j in range(n):
        if board[i][j] == "#":
            l = 0
            while valid(board, i, j, l + 1, m, n):
                l += 1
            if l > 0:
                res[l - 1] += 1

print(*res)