class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = rStart, cStart
        res = [(x, y)]
        l = 1
        d = 0
        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(l):
                    x += dx[d % 4]
                    y += dy[d % 4]
                    if 0 <= x < rows and 0 <= y < cols:
                        res.append((x, y))
                d += 1
            l += 1
        return res