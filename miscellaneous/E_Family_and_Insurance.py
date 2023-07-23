from collections import defaultdict

n, m = map(int, input().split())

p = list(map(int, input().split()))

graph = defaultdict(set)

for i in range(2, n + 1):
    graph[p[i - 2]].add(i)

ins = defaultdict(lambda: float('-inf'))

for _ in range(m):
    a, b = map(int, input().split())
    ins[a] = max(ins[a], b)

md = ins[1]

stack = [(1, 0, md)]

res = 0

while len(stack) > 0:
    curr, d, md = stack.pop()
    if d <= md:
        res += 1
    for j in graph[curr]:
        stack.append((j, d + 1, max(md, d + ins[j] + 1)))

print(res)