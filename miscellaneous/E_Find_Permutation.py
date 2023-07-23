from collections import defaultdict, deque

n, m = map(int, input().split())

graph = defaultdict(set)


for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].add(y)

def solve(graph, n, reverse):
    indegree = [0] * n

    for x in graph:
        for y in graph[x]:
            indegree[y] += 1

    q = deque()

    for i in range(n):
        if indegree[i] == 0:
            q.appendleft(i)

    if len(q) > 1:
        return False

    order = []

    while len(q) > 0:
        curr = q.pop()
        order.append(curr)
        for j in sorted(graph[curr], reverse = reverse):
            indegree[j] -= 1
            if indegree[j] == 0:
                q.appendleft(j)

    res = [-1] * n

    for i in range(len(order)):
        res[order[i]] = i + 1

    return res

a = solve(graph, n, False)
b = solve(graph, n, True)

if a and b and a == b:
    print("Yes")
    print(*a)
else:
    print("No")