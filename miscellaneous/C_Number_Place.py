from collections import defaultdict

board = []

for _ in range(9):
    board.append(list(map(int, input().split())))


def isValidSudoku(board):
    n = 9
    k = 3
    rowseen = defaultdict(set)
    colseen = defaultdict(set)
    cellseen = defaultdict(set)
    for i in range(n):
        for j in range(n):
            curr = board[i][j]
            if curr != ".":
                if curr in rowseen[i] or curr in colseen[j]:
                    return False
                rowseen[i].add(curr)
                colseen[j].add(curr)
                cell = (i // k, j // k)
                if curr in cellseen[cell]:
                    return False
                cellseen[cell].add(curr)
    return True

print("Yes" if isValidSudoku(board) else "No")