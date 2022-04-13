class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        op = []
        x, y = 0, 0
        while len(op) != m * n:
            op.append(mat[y][x])
            if (x + y) % 2 == 0:
                dx, dy = 1, -1
            else:
                dx, dy = -1, 1
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
                if (x + y) % 2 == 0:
                    if x < n - 1:
                        x += 1
                    else:
                        y += 1
                else:
                    if y < m - 1:
                        y += 1
                    else:
                        x += 1
            else:
                x += dx
                y += dy
        return op