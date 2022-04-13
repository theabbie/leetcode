class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        op = []
        x, y = 0, 0
        while len(op) != m * n:
            slope = (x + y) & 1
            op.append(mat[y][x])
            dx, dy = (-1, 1) if slope else (1, -1)
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
                if slope:
                    if y < m - 1:
                        y += 1
                    else:
                        x += 1
                else:
                    if x < n - 1:
                        x += 1
                    else:
                        y += 1
            else:
                x += dx
                y += dy
        return op