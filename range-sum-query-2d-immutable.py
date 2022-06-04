class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = matrix
        self.qsum = [[None for i in range(n)] for j in range(m)]
        
    def getSum(self, i, j):
        if i < 0 or j < 0:
            return 0
        if self.qsum[i][j] != None:
            return self.qsum[i][j]
        prev = self.getSum(i - 1, j - 1)
        row = self.getSum(i - 1, j)
        col = self.getSum(i, j - 1)
        res = row + col + self.matrix[i][j] - prev
        self.qsum[i][j] = res
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        c = self.getSum(row2, col2)
        l = self.getSum(row2, col1 - 1)
        t = self.getSum(row1 - 1, col2)
        s = self.getSum(row1 - 1, col1 - 1)
        return c - l - t + s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)