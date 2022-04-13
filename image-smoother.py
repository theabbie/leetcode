class Solution:
    def getNeighbors(self, row, col, m, n):
        neighbors = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i == row and j == col:
                    continue
                if i < 0 or i >= m:
                    continue
                if j < 0 or j >= n:
                    continue
                neighbors.append((i, j))
        return neighbors
    
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        imgcp = [row[:] for row in img]
        m = len(img)
        n = len(img[0])
        for i in range(m):
            for j in range(n):
                nb = self.getNeighbors(i, j, m, n)
                total = sum([imgcp[a][b] for a, b in nb]) + imgcp[i][j]
                num = len(nb) + 1
                img[i][j] = int(total/num)
        return img