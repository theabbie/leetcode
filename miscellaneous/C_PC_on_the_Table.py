m, n = map(int, input().split())

board = []

for _ in range(m):
    board.append(list(input()))

for i in range(m):
    for j in range(n - 1):
        if board[i][j] == board[i][j + 1] == 'T':
            board[i][j] = 'P'
            board[i][j + 1] = 'C'

print("\n".join("".join(r) for r in board))