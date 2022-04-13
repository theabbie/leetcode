class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        op = []
        mark = "X"
        ctr = 0
        direction = 0
        x, y = 0, 0
        while ctr < m * n:
            if matrix[x][y] != mark:
                ctr += 1
                op.append(matrix[x][y])
            matrix[x][y] = mark
            switch = False
            if direction == 0:
                if (y + 1) < n and matrix[x][y + 1] != mark:
                    y += 1
                else:
                    switch = True
            elif direction == 1:
                if (x + 1) < m and matrix[x + 1][y] != mark:
                    x += 1
                else:
                    switch = True
            elif direction == 2:
                if (y - 1) >= 0 and matrix[x][y - 1] != mark:
                    y -= 1
                else:
                    switch = True
            else:
                if (x + 1) >= 0 and matrix[x - 1][y] != mark:
                    x -= 1
                else:
                    switch = True
            if switch:
                direction = (direction + 1) % 4
        return op