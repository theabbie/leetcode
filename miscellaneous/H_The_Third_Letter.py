from collections import Counter, defaultdict, deque

t = int(input())

res = []

for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(set)
    indegree = Counter()
    for _ in range(m):
        a, b, d = map(int, input().split())
        a -= 1
        b -= 1
        if d < 0:
            a, b = b, a
            d = -d
        graph[a].add((b, d))
    valid = True
    pos = {}
    for i in graph:
        
    res.append("YES" if valid else "NO")

print(*res)