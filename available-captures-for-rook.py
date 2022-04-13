class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    ctr = 0
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        n = 0
                        while i + n * di >= 0 and i + n * di < 8 and j + n * dj >= 0 and j + n * dj < 8:
                            if board[i + n * di][j + n * dj] == 'B':
                                break
                            if board[i + n * di][j + n * dj] == 'p':
                                ctr += 1
                                break
                            n += 1
                    return ctr