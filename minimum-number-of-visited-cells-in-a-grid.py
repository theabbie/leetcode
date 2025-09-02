from sortedcontainers import SortedList

class Visiter:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.rows = [SortedList(range(n)) for _ in range(m)]
        self.cols = [SortedList(range(m)) for _ in range(n)]
    
    def visit(self, i, j):
        self.rows[i].discard(j)
        self.cols[j].discard(i)
    
    def right(self, i, j, k):
        sl = self.rows[i]
        idx = sl.bisect_left(j + 1)
        res = []
        while idx < len(sl) and sl[idx] <= j + k:
            res.append(sl[idx])
            idx += 1
        return [(i, c) for c in res]
    
    def down(self, i, j, k):
        sl = self.cols[j]
        idx = sl.bisect_left(i + 1)
        res = []
        while idx < len(sl) and sl[idx] <= i + k:
            res.append(sl[idx])
            idx += 1
        return [(r, j) for r in res]

    def get(self, i, j, k):
        return self.right(i, j, k) + self.down(i, j, k)

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque([(1, 0, 0)])
        v = Visiter(m, n)
        v.visit(0, 0)
        while q:
            d, i, j = q.pop()
            if (i, j) == (m - 1, n - 1):
                return d
            for x, y in v.get(i, j, grid[i][j]):
                v.visit(x, y)
                q.appendleft((d + 1, x, y))
        return -1