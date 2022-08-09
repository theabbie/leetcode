from collections import defaultdict

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def DFS(i, graph, v, ctr):
    for j in graph[i]:
        if j not in v:
            v.add(j)
            DFS(j, graph, v, ctr)
        else:
            ctr[0] += 1

visited = set()

res = 0

for i in range(1, n + 1):
    if i not in visited:
        v = {i}
        ctr = [0]
        DFS(i, graph, v, ctr)
        if ctr[0] == len(v) + 1:
            res += 1
        visited.update(v)

print(res)