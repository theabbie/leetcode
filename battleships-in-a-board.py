class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        visited = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" and (i, j) not in visited:
                    res += 1
                    visited.add((i, j))
                    l = 1
                    r = 1
                    u = 1
                    d = 1
                    while j - l >= 0 and board[i][j - l] == "X":
                        visited.add((i, j - l))
                        l += 1
                    while j + r < n and board[i][j + r] == "X":
                        visited.add((i, j + r))
                        r += 1
                    while i - u >= 0 and board[i - u][j] == "X":
                        visited.add((i - u, j))
                        u += 1
                    while i + d < m and board[i + d][j] == "X":
                        visited.add((i + d, j))
                        d += 1
        return res