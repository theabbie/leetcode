from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def key(g):
            res = 0
            for i in range(3):
                for j in range(3):
                    res = 10 * res + g[i][j]
            return res
        target = [[1] * 3 for _ in range(3)]
        q = deque([(grid, 0)])
        v = {key(grid)}
        while len(q) > 0:
            curr, steps = q.pop()
            if curr == target:
                return steps
            for i in range(3):
                for j in range(3):
                    if curr[i][j] > 1:
                        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            k = i + dx
                            l = j + dy
                            if 0 <= k < 3 and 0 <= l < 3:
                                newcurr = [[curr[i][j] for j in range(3)] for i in range(3)]
                                newcurr[i][j] -= 1
                                newcurr[k][l] += 1
                                newkey = key(newcurr)
                                if newkey not in v:
                                    v.add(newkey)
                                    q.appendleft((newcurr, steps + 1))
        return -1