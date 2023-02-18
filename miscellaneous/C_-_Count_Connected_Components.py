from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

graph = defaultdict(set)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

def DFS(graph, i, v):
    for j in graph[i]:
        if j not in v:
            v.add(j)
            DFS(graph, j, v)

res = 0

v = set()

for i in range(1, n + 1):
    if i not in v:
        res += 1
        v.add(i)
        DFS(graph, i, v)

print(res)