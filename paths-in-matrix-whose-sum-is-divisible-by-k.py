c = {}

def cache(fn):
    def inner(*args):
        args = tuple(args)
        if args in c:
            return c[args]
        c[args] = fn(*args)
        return c[args]
    return inner

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        M = 10 ** 9 + 7
        @cache
        def count(i, j, mod):
            if (i, j) == (m - 1, n - 1):
                return int((mod + grid[i][j]) % k == 0)
            res = (count(i + 1, j, (mod + grid[i][j]) % k) if i < m - 1 else 0) + (count(i, j + 1, (mod + grid[i][j]) % k) if j < n - 1 else 0)
            res %= M
            return res
        c.clear()
        return count(0, 0, 0)