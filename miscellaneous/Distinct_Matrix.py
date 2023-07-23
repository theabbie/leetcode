t = int(input())

def valid(mat, n):
    return len(set(mat) | set("".join([mat[i][j] for i in range(n)]) for j in range(n))) == 2 * n

for _ in range(t):
    n = int(input())
    res = []
    for i in range(n):
        curr = i ^ (i >> 1)
        row = []
        for j in range(n):
            if curr & (1 << j):
                row.append("1")
            else:
                row.append("0")
        res.append("".join(row))
    print("\n".join(res) if valid(res, n) else -1)