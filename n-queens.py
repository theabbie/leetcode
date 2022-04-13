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
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = self.getAllPos(set(), set(), set(), 0, n)
        op = []
        for q in queens:
            op.append([])
            for col in q:
                val = ["."] * n
                val[col] = "Q"
                op[-1].append("".join(val))
        return op