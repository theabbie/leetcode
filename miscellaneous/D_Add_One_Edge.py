from collections import defaultdict, deque

def bfs(graph, u):
    v = {u}
    q = deque([(u, 0)])
    mdist = 0
    while len(q) > 0:
        curr, d = q.pop()
        mdist = max(mdist, d)
        for j in graph[curr]:
            if j not in v:
                v.add(j)
                q.appendleft((j, d + 1))
    return mdist

n1, n2, m = map(int, input().split())

graph = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

print(bfs(graph, 1) + bfs(graph, n1 + n2) + 1)