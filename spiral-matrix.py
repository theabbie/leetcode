class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        op = []
        visited = set()
        direction = 0
        x, y = 0, 0
        while len(visited) < m * n:
            if (x, y) not in visited:
                op.append(matrix[x][y])
            visited.add((x, y))
            switch = False
            if direction == 0:
                if (y + 1) < n and (x, y + 1) not in visited:
                    y += 1
                else:
                    switch = True
            elif direction == 1:
                if (x + 1) < m and (x + 1, y) not in visited:
                    x += 1
                else:
                    switch = True
            elif direction == 2:
                if (y - 1) >= 0 and (x, y - 1) not in visited:
                    y -= 1
                else:
                    switch = True
            else:
                if (x + 1) >= 0 and (x - 1, y) not in visited:
                    x -= 1
                else:
                    switch = True
            if switch:
                direction = (direction + 1) % 4
        return op