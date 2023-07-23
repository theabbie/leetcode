t = int(input())

res = []

for _ in range(t):
    board = []
    for __ in range(8):
        board.append(input())
    pos = (-1, -1)
    for i in range(8):
        for j in range(8):
            if board[i][j] != "." and (i == 0 or board[i - 1][j] == "."):
                pos = (i, j)
                break
        if pos != (-1, -1):
            break
    curr = []
    x, y = pos
    while x < 8 and board[x][y] != ".":
        curr.append(board[x][y])
        x += 1
    res.append("".join(curr))

print(*res)