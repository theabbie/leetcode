def getmax(grid):
    m = len(grid)
    n = len(grid[0])
    res = 0
    resmove = (0, 0)
    for r in range(1 << m):
        for c in range(1 << n):
            curr = 0
            for i in range(m):
                for j in range(n):
                    val = grid[i][j]
                    if (r & (1 << i)) ^ (c & (1 << j)):
                        val = 1 - val
                    curr += val
            res = max(res, curr)
            if res == curr:
                resmove = (r, c)
    for i in range(m):
        for j in range(n):
            if (resmove[0] & (1 << i)) ^ (resmove[1] & (1 << j)):
                grid[i][j] = 1 - grid[i][j]
    print("{:b}".format(resmove[0]), "{:b}".format(resmove[1]))
    return res

grid = [
    [0, 0],
    [0, 1]
]

print(getmax(grid))

print("\n".join(" ".join(map(str, r)) for r in grid))