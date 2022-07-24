def findPath(i, j, k, n, res):
    if k == n * n:
        return True
    res[i][j] = k
    for dx in [-2, 2]:
        for dy in [-1, 1]:
            for x, y in [(i + dx, j + dy), (i + dy, j + dx)]:
                if 0 <= x < n and 0 <= y < n and res[x][y] == -1:
                    curr = findPath(x, y, k + 1, n, res)
                    if curr:
                        return True
    res[i][j] = -1
    return False

n = 4
res = [[-1] * n for _ in range(n)]
findPath(2, 2, 0, n, res)
print("\n".join(" ".join(map(lambda s: "{:2}".format(s), r)) for r in res))