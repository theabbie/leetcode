class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        M = 10 ** 9 + 7
        n = len(board)
        @lru_cache(maxsize = None)
        def dp(i, j):
            if (i, j) == (0, 0):
                return [0, 1]
            res = [float('-inf'), 0]
            for x, y in [(i - 1, j), (i, j - 1), (i - 1, j - 1)]:
                if x >= 0 and y >= 0 and board[x][y] != 'X':
                    nb = dp(x, y)
                    score = int(board[i][j] if board[i][j] not in 'ES' else 0) + nb[0]
                    if score == res[0]:
                        res[1] += nb[1]
                    elif score > res[0]:
                        res[0] = score
                        res[1] = nb[1]
            return [res[0] % M if res[0] != float('-inf') else res[0], res[1] % M]
        res = dp(n - 1, n - 1)
        if res[0] == float('-inf'):
            res[0] = 0
        return res