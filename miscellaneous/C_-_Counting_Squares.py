res = 0

points = []

def dist(a, b):
    return (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])

def isSquare(a, b, c, d):
    if dist(a, c) != dist(b, d):
        return False
    if a[0] + c[0] != b[0] + d[0] or a[1] + c[1] != b[1] + d[1]:
        return False
    if (c[1] - a[1]) * (d[1] - b[1]) != -(c[0] - a[0]) * (d[0] - b[0]):
        return False
    return True

for i in range(1, 10):
    s = input()
    for j in range(9):
        if s[j] == '#':
            points.append((i, j + 1))

points.sort()

n = len(points)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                if isSquare(points[i], points[j], points[l], points[k]):
                    res += 1

print(res)