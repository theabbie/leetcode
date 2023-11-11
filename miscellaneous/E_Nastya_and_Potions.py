from collections import defaultdict, deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    for i in p:
        c[i - 1] = 0
    graph = defaultdict(set)
    indegree = defaultdict(int)
    for i in range(n):
        curr = list(map(int, input().split()))
        for el in curr[1:]:
            graph[i].add(el - 1)
            indegree[el - 1] += 1
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.appendleft(i)
    order = []
    while len(q) > 0:
        curr = q.pop()
        order.append(curr)
        for j in graph[curr]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.appendleft(j)
    order.reverse()
    res = defaultdict(lambda: float('inf'))
    for el in order:
        curr = 0
        for j in graph[el]:
            curr += res[j]
        if len(graph[el]) == 0:
            curr = c[el]
        curr = min(curr, c[el])
        res[el] = curr
    print(*[res[i] for i in range(n)])