from collections import deque

dp = {}
initial = (1,) * 9
queue = deque([initial])
dp[initial] = 0
neighbors = [[] for _ in range(9)]
for i in range(9):
    r, c = i // 3, i % 3
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            neighbors[i].append(nr * 3 + nc)
while queue:
    state = queue.popleft()
    d = dp[state]
    for i in range(9):
        if state[i]:
            for j in neighbors[i]:
                ns = list(state)
                ns[i] -= 1
                ns[j] += 1
                ns = tuple(ns)
                if ns not in dp:
                    dp[ns] = d + 1
                    queue.append(ns)

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        state = tuple(grid[i][j] for i in range(3) for j in range(3))
        return dp[state]