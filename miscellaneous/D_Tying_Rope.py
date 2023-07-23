from collections import defaultdict

n, m = map(int, input().split())

graph = defaultdict(lambda: [-1, -1])

for _ in range(m):
    a, b, c, d = input().split()
    if b == 'R':
        graph[int(a)][0] = int(c)
    if b == 'B':
        graph[int(a)][1] = int(c)
    if d == 'R':
        graph[int(c)][0] = int(a)
    if d == 'B':
        graph[int(c)][1] = int(a)

print(graph)