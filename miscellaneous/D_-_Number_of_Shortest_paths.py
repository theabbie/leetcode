from collections import defaultdict, deque

M = 10 ** 9 + 7

n, m = map(int, input().split())

graph = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

dist = defaultdict(lambda: float('inf'))
ctr = defaultdict(int)
ctr[1] = 1

q = deque([(1, 0)])

while len(q) > 0:
    curr, currdist = q.pop()
    for j in graph[curr]:
        if dist[j] > currdist + 1:
            dist[j] = currdist + 1
            ctr[j] = ctr[curr]
            q.appendleft((j, currdist + 1))
        elif dist[j] == currdist + 1:
            ctr[j] = (ctr[j] + ctr[curr]) % M

print(ctr[n])