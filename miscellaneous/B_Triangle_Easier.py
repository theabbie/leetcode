n, m = map(int, input().split())

res = 0

edges = set()

for _ in range(m):
    u, v = map(int, input().split())
    edges.add((u - 1, v - 1))
    edges.add((v - 1, u - 1))

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (i, j) in edges and (j, k) in edges and (i, k) in edges:
                res += 1

print(res)