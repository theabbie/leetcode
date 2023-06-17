from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if forest[0][0] == 0:
            return -1
        m = len(forest)
        n = len(forest[0])
        vals = set()
        for i in range(m):
            for j in range(n):
                if forest[i][j] not in {0, 1}:
                    vals.add((forest[i][j], i, j))
        vals = [(0, 0, 0)] + sorted(vals)
        k = len(vals)
        res = 0
        for pos in range(k - 1):
            vv, ii, jj = vals[pos]
            q = deque([(ii, jj, 0)])
            v = {(ii, jj)}
            found = False
            while len(q) > 0:
                i, j, d = q.pop()
                if forest[i][j] == vals[pos + 1][0]:
                    res += d
                    found = True
                    break
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and forest[x][y] != 0 and (x, y) not in v:
                        v.add((x, y))
                        q.appendleft((x, y, d + 1))
            if not found:
                return -1
        return res