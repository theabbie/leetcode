import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n = int(input())

graph = defaultdict(set)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

res = 1

def DFS(a, graph, v):
    global res
    res = max(res, a)
    for b in graph[a]:
        if b not in v:
            v.add(b)
            DFS(b, graph, v)

v = {1}
DFS(1, graph, v)
print(res)