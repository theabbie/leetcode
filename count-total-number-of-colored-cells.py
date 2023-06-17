class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return 4 * (n - 1) + self.coloredCells(n - 1)