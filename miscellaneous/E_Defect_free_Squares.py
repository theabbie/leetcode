def create_grid(h, w, points):
    grid = [[0 for _ in range(w)] for _ in range(h)]
    for point in points:
        x, y = point
        grid[x][y] = 1
    return grid

def compute_prefix_sums(grid):
    h, w = len(grid), len(grid[0])
    prefix_sums = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            prefix_sums[i][j] = grid[i][j]
            if i > 0:
                prefix_sums[i][j] += prefix_sums[i - 1][j]
            if j > 0:
                prefix_sums[i][j] += prefix_sums[i][j - 1]
            if i > 0 and j > 0:
                prefix_sums[i][j] -= prefix_sums[i - 1][j - 1]
    return prefix_sums

def query_sum(prefix_sums, x1, y1, x2, y2):
    total_sum = prefix_sums[x2][y2]
    if x1 > 0:
        total_sum -= prefix_sums[x1 - 1][y2]
    if y1 > 0:
        total_sum -= prefix_sums[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        total_sum += prefix_sums[x1 - 1][y1 - 1]
    return total_sum

h, w, n = map(int, input().split())

points = []
for _ in range(n):
    a, b = map(int, input().split())
    points.append((a - 1, b - 1))

grid = create_grid(h, w, points)
prefix_sums = compute_prefix_sums(grid)

print(query_sum(prefix_sums, 0, 0, 1, 2))