class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            x = i
            y = 0
            p = []
            while x < n and y < n:
                p.append(grid[x][y])
                x += 1
                y += 1
            p.sort()
            x = i
            y = 0
            while x < n and y < n:
                grid[x][y] = p.pop()
                x += 1
                y += 1
        for i in range(1, n):
            x = 0
            y = i
            p = []
            while x < n and y < n:
                p.append(grid[x][y])
                x += 1
                y += 1
            p.sort(reverse = True)
            x = 0
            y = i
            while x < n and y < n:
                grid[x][y] = p.pop()
                x += 1
                y += 1
        return grid