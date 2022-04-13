class Solution:
    def getAllPos(self, usedCols, usedPosDiag, usedNegDiag, i, n):
        if i >= n:
            return [[]]
        op = []
        for j in range(n):
            if j not in usedCols and (i + j) not in usedPosDiag and (i - j) not in usedNegDiag:
                val = self.getAllPos(usedCols.union({j}), usedPosDiag.union({i + j}), usedNegDiag.union({i - j}), i + 1, n)
                op += [[j] + v for v in val]
        return op
    
    def getRow(self, i, n):
        val = ["."] * n
        val[i] = "Q"
        return "".join(val)
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = self.getAllPos(set(), set(), set(), 0, n)
        return [[self.getRow(i, n) for i in q] for q in queens]