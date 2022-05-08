import random

class Solution:
    def getPos(self, board, i, j):
        pos = set(map(str, range(1, 10)))
        ci, cj = i - i % 3, j - j % 3
        for a in range(3):
            for b in range(3):
                if board[ci + a][cj + b] != "." and board[ci + a][cj + b] in pos:
                    pos.remove(board[ci + a][cj + b])
        for a in range(9):
            if board[i][a] in pos:
                pos.remove(board[i][a])
            if board[a][j] in pos:
                pos.remove(board[a][j])
        pos = list(pos)
        random.shuffle(pos)
        return pos
    
    def solve(self, board, spi):
        if spi >= len(self.spaces):
            return board
        if spi < len(self.spaces):
            i, j = self.spaces[spi]
            pos = self.getPos(board, i, j)
            currboard = [[b for b in row] for row in board]
            for p in pos:
                currboard[i][j] = p
                currsolution = self.solve(currboard, spi + 1)
                if currsolution:
                    return currsolution
        return False
    
    def solveSudoku(self, board):
        self.spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    self.spaces.append((i, j))
        return self.solve(board, 0)

board = [["."] * 9 for _ in range(9)]
print("\n".join([" ".join(row) for row in Solution().solveSudoku(board)]))
