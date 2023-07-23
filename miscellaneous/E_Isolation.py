from collections import defaultdict

n, q = map(int, input().split())

graph = defaultdict(set)

ctr = n

res = []

def diff(old, new):
    if old != 0 and new == 0:
        return 1
    if old == 0 and new != 0:
        return -1
    return 0

for _ in range(q):
    curr = list(map(int, input().split()))
    if curr[0] == 1:
        u, v = curr[1] - 1, curr[2] - 1
        oldusize = len(graph[u])
        oldvsize = len(graph[v])
        graph[u].add(v)
        graph[v].add(u)
        newusize = len(graph[u])
        newvsize = len(graph[v])
        ctr += diff(oldusize, newusize)
        ctr += diff(oldvsize, newvsize)
    if curr[0] == 2:
        u = curr[1] - 1
        oldusize = len(graph[u])
        for j in list(graph[u]):
            oldsize = len(graph[j])
            graph[j].remove(u)
            graph[u].remove(j)
            newsize = len(graph[j])
            ctr += diff(oldsize, newsize)
        newusize = len(graph[u])
        ctr += diff(oldusize, newusize)
    res.append(str(ctr))

print("\n".join(res))