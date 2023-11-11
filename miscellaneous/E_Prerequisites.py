from collections import deque

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    curr = list(map(int, input().split()))
    for j in curr[1:]:
        graph[i].append(j - 1)

q = deque([0])

v = {0}

res = []

while len(q) > 0:
    curr = q.pop()
    res.append(curr + 1)
    for j in graph[curr]:
        if j not in v:
            v.add(j)
            q.appendleft(j)

res.reverse()

res.pop()

print(*res)