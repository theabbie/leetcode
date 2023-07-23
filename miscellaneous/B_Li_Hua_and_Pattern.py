t = int(input())

class Solution:
    def verticalFlip(self, matrix, n):
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    
    def diagonalFlip(self, matrix, n):
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def rotate(self, matrix):
        n = len(matrix)
        self.verticalFlip(matrix, n)
        self.diagonalFlip(matrix, n)

for _ in range(t):
    n, k = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    image = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            image[i][j] = (i, j)
    Solution().rotate(image)
    Solution().rotate(image)
    curr = 0
    eq = False
    for i in range(n):
        for j in range(n):
            if image[i][j] == (i, j):
                eq = True
            if board[image[i][j][0]][image[i][j][1]] != board[i][j]:
                curr += 1
                board[image[i][j][0]][image[i][j][1]] = board[i][j]
    print("YES" if (curr <= k and (eq or (k - curr) % 2 == 0)) else "NO")