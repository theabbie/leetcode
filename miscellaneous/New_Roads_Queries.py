n, m, q = map(int, input().split())

parent = list(range(n + 1))
time = [{} for _ in range(n + 1)]

t = 1

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    u = find(x)
    v = find(y)
    if u != v:
        parent[v] = u
        print(u, v, t)

for _ in range(m):
    a, b = map(int, input().split())
    union(min(a, b), max(a, b))
    t += 1

for _ in range(q):
    a, b = map(int, input().split())
    a = find(a)
    b = find(b)
    if b in time[a]:
        print(time[a][b])
    elif a in time[b]:
        print(time[b][a])
    else:
        print(-1)