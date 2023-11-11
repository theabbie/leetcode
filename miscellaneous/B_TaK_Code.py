m, n = map(int, input().split())

board = []

for _ in range(m):
    board.append(input())

target = """###.?????
###.?????
###.?????
....?????
?????????
?????....
?????.###
?????.###
?????.###""".split("\n")

def check(i, j):
    for x in range(9):
        for y in range(9):
            if target[x][y] == "?":
                continue
            if board[i + x][j + y] != target[x][y]:
                return False
    return True

for i in range(m - 8):
    for j in range(n - 8):
        if check(i, j):
            print(i + 1, j + 1)