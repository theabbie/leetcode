from collections import defaultdict, deque

t = int(input())

for _ in range(t):
    input()
    n, m = map(int, input().split())
    indegree = [0] * n
    graph = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        indegree[u - 1] += 1
        indegree[v - 1] += 1
        graph[u - 1].add(v - 1)
        graph[v - 1].add(u - 1)
    x = indegree.count(4)
    y = indegree.count(2)
    if max(indegree) != 4 or x + y != n or y != x * (x - 1):
        print("NO")
        continue
    mdeg = 4
    k = indegree.count(mdeg)
    q = deque()
    v = set()
    for i in range(n):
        if indegree[i] == mdeg:
            q.appendleft((i, i))
            v.add(i)
    reachable = [set() for i in range(n)]
    while len(q) > 0:
        curr, source = q.pop()
        reachable[source].add(curr)
        for j in graph[curr]:
            if j not in v:
                q.appendleft((j, source))
                v.add(j)
    res = True
    for i in range(n):
        if indegree[i] == mdeg:
            ctr = 0
            for j in graph[i]:
                if indegree[j] != mdeg:
                    ctr += 1
            if ctr != 2:
                res = False
                break
            for j in reachable[i]:
                if j == i and indegree[j] != 4:
                    res = False
                    break
                if j != i and indegree[j] != 2:
                    res = False
                    break
        if not res:
            break
    indegreecenter = [0] * n
    edges = set()
    for i in range(n):
        if indegree[i] == mdeg:
            for j in graph[i]:
                if indegree[j] == mdeg:
                    edges.add((min(i, j), max(i, j)))
                    indegreecenter[j] += 1
    if len(edges) != k:
        res = False
    for i in range(n):
        if indegree[i] == mdeg and indegreecenter[i] != 2:
            res = False
            break
    print("YES" if res else "NO")