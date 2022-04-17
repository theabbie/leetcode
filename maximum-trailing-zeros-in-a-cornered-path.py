class Solution:
    def num5divs(self, num):
        t = 0
        f = 0
        while num % 5 == 0:
            num = num // 5
            f += 1
        while num % 2 == 0:
            num = num // 2
            t += 1
        return (t, f)
    
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vertprefix = [[(0, 0)] for i in range(n)]
        horprefix = [[(0, 0)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = self.num5divs(grid[i][j])
                a, b = grid[i][j]
                ha, hb = horprefix[i][-1]
                va, vb = vertprefix[j][-1]
                horprefix[i].append((ha + a, hb + b))
                vertprefix[j].append((va + a, vb + b))
        maxtrail = 0
        for i in range(m):
            for j in range(n):
                hors = [vertprefix[j][i], (vertprefix[j][-1][0] - vertprefix[j][i + 1][0], vertprefix[j][-1][1] - vertprefix[j][i + 1][1])]
                verts = [horprefix[i][j], (horprefix[i][-1][0] - horprefix[i][j + 1][0], horprefix[i][-1][1] - horprefix[i][j + 1][1])]
                for ha, hb in hors:
                    for va, vb in verts:
                        a, b = grid[i][j]
                        maxtrail = max(maxtrail, min(a + ha + va, b + hb + vb))
        return maxtrail