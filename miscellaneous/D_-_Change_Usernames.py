from collections import defaultdict, Counter, deque

n = int(input())

graph = defaultdict(set)

for _ in range(n):
    a, b = input().split()
    graph[a].add(b)

indegree = Counter()

for el in graph:
    for j in graph[el]:
        indegree[j] += 1

q = deque()

for el in graph:
    if indegree[el] == 0:
        q.appendleft(el)

l = 0

while len(q) > 0:
    curr = q.pop()
    l += 1
    for j in graph[curr]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.appendleft(j)

print("Yes" if l == len(graph) else "No")