from collections import Counter

t = int(input())

def countdist(mat, n):
    vals = set()
    getval = lambda i, j: mat[i][j]
    for i in range(n):
        for j in range(n):
            if i + 1 < n:
                vals.add(abs(getval(i, j) - getval(i + 1, j)))
            if j + 1 < n:
                vals.add(abs(getval(i, j) - getval(i, j + 1)))
    return len(vals)

def getmat(mat, n, i, j, diffs, unused):
    if len(diffs) > 0 and max(diffs.values()) > 3:
        return False
    if i >= n:
        return len(diffs) + 1 == n * n
    for el in sorted(unused):
        mat[i][j] = el
        newdiffs = Counter()
        if i > 0:
            newdiffs[abs(el - mat[i - 1][j])] += 1
        if j > 0:
            newdiffs[abs(el - mat[i][j - 1])] += 1
        if j < n - 1 and getmat(mat, n, i, j + 1, diffs | newdiffs, unused - {el}):
            return True
        if j == n - 1 and getmat(mat, n, i + 1, 0, diffs | newdiffs, unused - {el}):
            return True
    return False

for _ in range(t):
    n = int(input())
    mat = [[-1] * n for _ in range(n)]
    getmat(mat, n, 0, 0, Counter(), set(range(1, n * n + 1)))
    print("\n".join(" ".join(map(str, r)) for r in mat))