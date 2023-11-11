from collections import defaultdict

def is_bipartite(graph, n):
    color = [-1] * n
    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            stack = [start]
            while stack:
                parent = stack.pop()
                for child in graph[parent]:
                    if color[child] == -1:
                        color[child] = 1 - color[parent]
                        stack.append(child)
                    elif color[parent] == color[child]:
                        return False
    return True

n, m = map(int, input().split())

pos = defaultdict(lambda: [[], []])

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(m):
    a[i] -= 1
    b[i] -= 1

graph = [[] for _ in range(n)]

for i in range(m):
    graph[a[i]].append(b[i])
    graph[b[i]].append(a[i])

print("Yes" if is_bipartite(graph, n) else "No")