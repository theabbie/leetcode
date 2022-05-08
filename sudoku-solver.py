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
        return pos
    
    def solve(self, board, spi):
        if spi >= len(self.spaces):
            return True
        if spi < len(self.spaces):
            i, j = self.spaces[spi]
            pos = self.getPos(board, i, j)
            for p in pos:
                board[i][j] = p
                currsolution = self.solve(board, spi + 1)
                if currsolution:
                    return True
                else:
                    board[i][j] = "."
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    self.spaces.append((i, j))
        self.solve(board, 0)