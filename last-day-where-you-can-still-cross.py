from collections import deque, defaultdict

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        p = len(cells)
        pos = defaultdict(lambda: p + 1)
        for i in range(p):
            pos[(cells[i][0] - 1, cells[i][1] - 1)] = i
        mat = lambda i, j, x: int(pos[(i, j)] < x)
        beg = 0
        end = p
        res = beg
        while beg <= end:
            mid = (beg + end) // 2
            reach = False
            q = deque()
            v = set()
            for j in range(col):
                if mat(0, j, mid) == 0:
                    q.appendleft((0, j))
                    v.add((0, j))
            while len(q) > 0:
                i, j = q.pop()
                if i == row - 1:
                    reach = True
                    break
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < row and 0 <= y < col and mat(x, y, mid) == 0 and (x, y) not in v:
                        v.add((x, y))
                        q.appendleft((x, y))
            if reach:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res