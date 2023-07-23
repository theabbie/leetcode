from collections import defaultdict

m, n = map(int, input().split())

board = []

for _ in range(m):
    board.append(input())

mp = {"s": "n", "n": "u", "u": "k", "k": "e", "e": "s"}

graph = defaultdict(set)

for i in range(m):
    for j in range(n):
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n:
                if mp.get(board[i][j], -1) == board[x][y]:
                    graph[(i, j)].add((x, y))

def check(graph):
    stack = [(0, 0)]
    v = {(0, 0)}
    while len(stack) > 0:
        curr = stack.pop()
        if curr == (m - 1, n - 1):
            return "Yes"
        for j in graph[curr]:
            if j not in v:
                v.add(j)
                stack.append(j)
    return "No"

print(check(graph))