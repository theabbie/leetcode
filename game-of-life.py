class Solution:
    def getNeighbors(self, i, j, m, n):
        neighbors = []
        for a in range(i - 1, i + 2):
            for b in range(j - 1, j + 2):
                if a == i and b == j:
                    continue
                if a < 0 or a >= m:
                    continue
                if b < 0 or b >= n:
                    continue
                neighbors.append((a, b))
        return neighbors
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        shifts = set()
        for i in range(m):
            for j in range(n):
                curr = board[i][j]
                neighbors = self.getNeighbors(i, j, m, n)
                num = sum([board[x][y] for x, y in neighbors])
                if curr == 1:
                    if num < 2 or num > 3:
                        shifts.add((i, j))
                else:
                    if num == 3:
                        shifts.add((i, j))
        for i, j in shifts:
            board[i][j] = 1 - board[i][j]