from collections import defaultdict, deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    graph = defaultdict(lambda: [set(), set()])
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1][c[v - 1]].add(v - 1)
        graph[v - 1][c[u - 1]].add(u - 1)
    q = deque([(0, n - 1, 0)])
    v = {(0, n - 1)}
    res = -1
    while len(q) > 0:
        a, b, steps = q.pop()
        if a == n - 1 and b == 0:
            res = steps
            break
        for i in graph[a][0]:
            for j in graph[b][1]:
                if (i, j) not in v:
                    v.add((i, j))
                    q.appendleft((i, j, steps + 1))
        for i in graph[a][1]:
            for j in graph[b][0]:
                if (i, j) not in v:
                    v.add((i, j))
                    q.appendleft((i, j, steps + 1))
    print(res)