import sys

sys.setrecursionlimit(10 ** 6)

def count(board, i, j, m, n, used):
    if (i, j) == (m - 1, n - 1):
        return 1
    res = 0
    for x, y in [(i + 1, j), (i, j + 1)]:
        if 0 <= x < m and 0 <= y < n:
            if board[x][y] not in used:
                used.add(board[x][y])
                res += count(board, x, y, m, n, used)
                used.remove(board[x][y])
    return res

m, n = map(int, input().split())

board = []

for _ in range(m):
    board.append(list(map(int, input().split())))

print(count(board, 0, 0, m, n, {board[0][0]}))