from collections import defaultdict, deque

n, d = map(int, input().split())

points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y, i))

res = ["No"] * n

graph = defaultdict(set)

for i in range(n):
    for j in range(i + 1, n):
        if (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2 <= d * d:
            graph[i].add(j)
            graph[j].add(i)

q = deque([0])

res[0] = "Yes"

while len(q) > 0:
    curr = q.pop()
    for j in graph[curr]:
        if res[j] == "No":
            res[j] = "Yes"
            q.appendleft(j)

print("\n".join(res))