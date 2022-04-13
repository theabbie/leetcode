class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1 for i in range(n)] for j in range(n)]
        ctr = 0
        direction = 0
        x, y = 0, 0
        while ctr < n * n:
            if matrix[x][y] == -1:
                ctr += 1
                matrix[x][y] = ctr
            switch = False
            if direction == 0:
                if (y + 1) < n and matrix[x][y + 1] == -1:
                    y += 1
                else:
                    switch = True
            elif direction == 1:
                if (x + 1) < n and matrix[x + 1][y] == -1:
                    x += 1
                else:
                    switch = True
            elif direction == 2:
                if (y - 1) >= 0 and matrix[x][y - 1] == -1:
                    y -= 1
                else:
                    switch = True
            else:
                if (x - 1) >= 0 and matrix[x - 1][y] == -1:
                    x -= 1
                else:
                    switch = True
            if switch:
                direction = (direction + 1) % 4
        return matrix