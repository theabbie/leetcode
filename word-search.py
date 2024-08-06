class Solution:
    def getNeighbors(self, i, j, m, n):
        nb = []
        if i > 0:
            nb.append((i - 1, j))
        if i < m - 1:
            nb.append((i + 1, j))
        if j > 0:
            nb.append((i, j - 1))
        if j < n - 1:
            nb.append((i, j + 1))
        return nb
    
    def isPossible(self, board, m, n, pos, word, i, used):
        if i == len(word) - 1:
            return True
        neighbors = self.getNeighbors(pos[0], pos[1], m, n)
        for a, b in neighbors:
            if (a, b) not in used and board[a][b] == word[i + 1]:
                if self.isPossible(board, m, n, (a, b), word, i + 1, used.union({(a, b)})):
                    return True
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wlen = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.isPossible(board, m, n, (i, j), word, 0, {(i, j)}):
                        return True
        return False