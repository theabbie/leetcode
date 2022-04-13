# class Solution:
#     def isAdjacent(a, b, c, d):
#         if a == c and abs(b - d) == 1:
#             return True
#         if b == d and abs(a - c) == 1:
#             return True
#         return False
    
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         m = len(board)
#         n = len(board[0])
#         wlen = len(word)
#         pos = [[] for c in word]
#         for i in range(m):
#             for j in range(n):
#                 for k in range(wlen):
#                     if word[k] == board[i][j]:
#                         pos[k].append((i, j))
#         paths = [[i] for i in pos[0]]
#         while len(paths) > 0:
#             curr = paths.pop(0)
#             currlen = len(curr)
#             lastcell = curr[-1]
#             if currlen == wlen:
#                 return True
#             if currlen < wlen:
#                 for x, y in pos[currlen + 1]:
#                     if (x, y) not in curr and self.isAdjacent(lastcell, x, y):
#                         paths.append(curr + [(x, y)])
#         return False

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