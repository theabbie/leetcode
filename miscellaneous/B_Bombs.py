r, c = map(int, input().split())

board = []

for _ in range(r):
    board.append(list(input()))

bombs = set()

for i in range(r):
    for j in range(c):
        if board[i][j] != "#" and board[i][j] != ".":
            bombs.add((i, j, int(board[i][j])))

for i in range(r):
    for j in range(c):
        for x, y, d in bombs:
            if abs(i - x) + abs(j - y) <= d:
                board[i][j] = "."
                break

print("\n".join("".join(row) for row in board))