from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].add(v - 1)
        graph[v - 1].add(u - 1)
    