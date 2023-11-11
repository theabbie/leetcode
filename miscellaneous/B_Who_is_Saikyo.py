import sys

sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())

parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

for _ in range(m):
    a, b = map(int, input().split())
    parent[b - 1] = find(a - 1)

all = []

for i in range(n):
    ctr = 0
    for j in range(n):
        if find(j) == i:
            ctr += 1
    if ctr == n:
        all.append(i)

if len(all) == 1:
    print(1 + all[0])
else:
    print(-1)