class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        graph = {}
        for i in range(n * n):
            row = i // n
            col = i % n
            if row % 2 == 1:
                col = n - col - 1
            row = n - row - 1
            if board[row][col] != -1:
                graph[i + 1] = board[row][col]
        visited = set()
        paths = [(1, 0)]
        i = 0
        while i < len(paths):
            curr, moves = paths[i]
            if curr == n * n:
                return moves
            for jump in range(curr + 1, min(curr + 7, (n * n) + 1)):
                if jump not in visited:
                    visited.add(jump)
                    paths.append((graph.get(jump, jump), moves + 1))
            i += 1
        return -1