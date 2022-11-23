from collections import defaultdict, deque

t = int(input())

def bfs(graph, x):
    q = deque([(x, 0)])
    v = {x}
    xor = {}
    while len(q) > 0:
        curr, xorval = q.pop()
        xor[curr] = xorval
        for j, w in graph[curr]:
            if j not in v:
                v.add(j)
                q.appendleft((j, xorval ^ w))
    return xor

for _ in range(t):
    n, a, b = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        graph[u].add((v, w))
        graph[v].add((u, w))
    xor = bfs(graph, b)
    bvals = set()
    for i in graph:
        if i != b:
            bvals.add(xor[i])
    pos = xor[a] == 0
    q = deque([(a, 0)])
    v = {a, b}
    while len(q) > 0:
        curr, xorval = q.pop()
        if xorval in bvals:
            pos = True
            break
        for j, w in graph[curr]:
            if j not in v:
                v.add(j)
                q.appendleft((j, xorval ^ w))
    print("YES" if pos else "NO")