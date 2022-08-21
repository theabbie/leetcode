class Solution:
    def solve(self, board, i, n, usedRows, usedPosDiag, usedNegDiag, res):
        if i >= n:
            res.append(["".join(row) for row in board])
            return
        for j in range(n):
            if j not in usedRows and i - j not in usedPosDiag and i + j not in usedNegDiag:
                usedRows.add(j)
                usedPosDiag.add(i - j)
                usedNegDiag.add(i + j)
                board[i][j] = "Q"
                self.solve(board, i + 1, n, usedRows, usedPosDiag, usedNegDiag, res)
                board[i][j] = "."
                usedRows.remove(j)
                usedPosDiag.remove(i - j)
                usedNegDiag.remove(i + j)
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        self.solve(board, 0, n, set(), set(), set(), res)
        return res