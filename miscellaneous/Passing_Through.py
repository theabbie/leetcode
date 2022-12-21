from collections import defaultdict, Counter

t = int(input())

for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    graph = defaultdict(set)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].add(b - 1)
        graph[b - 1].add(a - 1)
    ctr = Counter(c)