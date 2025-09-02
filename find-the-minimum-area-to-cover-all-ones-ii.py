class Solution:
    def minimumSum(self, grid):
        inf = float('inf')
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        def minarea(g, si, ei, sj, ej):
            if si > ei:
                return 0
            if sj > ej:
                return 0
            sr = inf
            er = float('-inf')
            sc = inf
            ec = float('-inf')
            found = False
            i = si
            while i <= ei:
                j = sj
                while j <= ej:
                    if g[i][j]:
                        if i < sr:
                            sr = i
                        if i > er:
                            er = i
                        if j < sc:
                            sc = j
                        if j > ec:
                            ec = j
                        found = True
                    j += 1
                i += 1
            if not found:
                return 0
            h = er - sr + 1
            w = ec - sc + 1
            return h * w
        res = inf
        i = 0
        while i < m:
            one = minarea(grid, 0, i, 0, n - 1)
            j = 0
            while j < n:
                two = minarea(grid, i + 1, m - 1, 0, j)
                three = minarea(grid, i + 1, m - 1, j + 1, n - 1)
                s = one + two + three
                if s < res:
                    res = s
                j += 1
            i += 1
        j = 0
        while j < n:
            one = minarea(grid, 0, m - 1, 0, j)
            i = 0
            while i < m:
                two = minarea(grid, 0, i, j + 1, n - 1)
                three = minarea(grid, i + 1, m - 1, j + 1, n - 1)
                s = one + two + three
                if s < res:
                    res = s
                i += 1
            j += 1
        j = n - 1
        while j >= 0:
            one = minarea(grid, 0, m - 1, j + 1, n - 1)
            i = 0
            while i < m:
                two = minarea(grid, 0, i, 0, j)
                three = minarea(grid, i + 1, m - 1, 0, j)
                s = one + two + three
                if s < res:
                    res = s
                i += 1
            j -= 1
        i = m - 1
        while i >= 0:
            one = minarea(grid, i + 1, m - 1, 0, n - 1)
            j = 0
            while j < n:
                two = minarea(grid, 0, i, 0, j)
                three = minarea(grid, 0, i, j + 1, n - 1)
                s = one + two + three
                if s < res:
                    res = s
                j += 1
            i -= 1
        i = 0
        while i < m:
            j = i + 1
            while j < m:
                one = minarea(grid, 0, i, 0, n - 1)
                two = minarea(grid, i + 1, j, 0, n - 1)
                three = minarea(grid, j + 1, m - 1, 0, n - 1)
                s = one + two + three
                if s < res:
                    res = s
                j += 1
            i += 1
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                one = minarea(grid, 0, m - 1, 0, i)
                two = minarea(grid, 0, m - 1, i + 1, j)
                three = minarea(grid, 0, m - 1, j + 1, n - 1)
                s = one + two + three
                if s < res:
                    res = s
                j += 1
            i += 1
        return res