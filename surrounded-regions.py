class Solution:
    def DFS(self, board, v, i, j, m, n):
        v.add((i, j))
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= i + di < m and 0 <= j + dj < n:
                if board[i + di][j + dj] == "O" and (i + di, j + dj) not in v:
                    self.DFS(board, v, i + di, j + dj, m, n)
    
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    v = set()
                    self.DFS(board, v, i, j, m, n)
                    isEnclosed = True
                    for x, y in v:
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            isEnclosed = False
                            break
                    if isEnclosed:
                        for x, y in v:
                            board[x][y] = "X"