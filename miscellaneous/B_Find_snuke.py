m, n = map(int, input().split())

def check(board):
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == "s":
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    curr = []
                    found = True
                    for p in range(5):
                        x = i + p * dx
                        y = j + p * dy
                        if 0 <= x < m and 0 <= y < n:
                            if board[x][y] != "snuke"[p]:
                                found = False
                                break
                            curr.append((x + 1, y + 1))
                        else:
                            found = False
                            break
                    if found:
                        return curr
    return False

board = []

for _ in range(m):
    board.append(input())

res = check(board)

print("\n".join(f"{a} {b}" for a, b in res))