board = []

for _ in range(8):
    board.append(input())

pos = (0, 0)

for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            pos = (j, 8 - i)

print(f"{chr(ord('a') + pos[0])}{pos[1]}")