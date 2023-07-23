from collections import defaultdict, deque

n = int(input())

ctr = [0] * n
graph = defaultdict(set)

for _ in range(n - 2):
    a, b, c = map(int, input().split())
    graph[a - 1].update({b - 1, c - 1})
    graph[b - 1].update({a - 1, c - 1})
    graph[c - 1].update({a - 1, b - 1})
    ctr[a - 1] += 1
    ctr[b - 1] += 1
    ctr[c - 1] += 1

print(ctr, graph)