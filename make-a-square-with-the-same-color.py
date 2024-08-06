class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                b = w = 0
                for x in range(2):
                    for y in range(2):
                        if grid[i + x][j + y] == 'B':
                            b += 1
                        if grid[i + x][j + y] == 'W':
                            w += 1
                if b == 4 or w == 4:
                    return True
                if b == 1 or w == 1:
                    return True
        return False