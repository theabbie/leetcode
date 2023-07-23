from collections import defaultdict

t = int(input().split())

for _ in range(t):
    n, m, k = map(int, input().split())
    x = list(map(int, input().split()))
    d = list(map(int, input().split()))
    graph = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    
    