n = int(input())

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

def check(a, b):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                if b[i][j] != 1:
                    return False
    return True

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

pos = False

for _ in range(4):
    if check(a, b):
        pos = True
        break
    Solution().rotate(b)

print("Yes" if pos else "No")