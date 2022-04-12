class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        luckyRows = set()
        luckyCols = set()
        for i in range(m):
            j = min(range(n), key = lambda x: matrix[i][x])
            luckyRows.add((i, j))
        for j in range(n):
            i = max(range(m), key = lambda x: matrix[x][j])
            luckyCols.add((i, j))
        lucky = set.intersection(luckyRows, luckyCols)
        return [matrix[i][j] for i, j in lucky]