from collections import defaultdict, deque

t = int(input())

def BFS(graph, i):
    q = deque([(i, 0)])
    dist = {}
    dist[i] = 0
    while len(q) > 0:
        curr, d = q.pop()
        for j in graph[curr]:
            if dist.get(j, float('inf')) > d + 1:
                dist[j] = d + 1
                q.appendleft((j, d + 1))
    res = max(dist.keys(), key = lambda i: dist[i])
    return (res, dist)

for _ in range(t):
    n, q = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    x, dx = BFS(graph, 1)
    y, dy = BFS(graph, x)
    z, dz = BFS(graph, y)
    res = []
    for _ in range(q):
        m = int(input())
        vals = list(map(int, input().split()))
        curr = float('-inf')
        for v in vals:
            curr = max(curr, dy[v], dz[v])
        res.append(str(curr))
    print("\n".join(res))